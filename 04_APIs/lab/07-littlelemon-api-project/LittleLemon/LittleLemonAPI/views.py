from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Cart, Category, MenuItem, Order, OrderItem
from .permissions import IsManager, is_manager
from .serializers import CartSerializer, CategorySerializer, MenuItemSerializer, OrderSerializer, UserSerializer


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        # Anyone with a token can browse categories; only managers can add one.
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsManager()]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category', 'featured']  # ?category=<id>&featured=true
    ordering_fields = ['price', 'title']  # ?ordering=price / ?ordering=-price
    search_fields = ['title']  # ?search=<text>

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsManager()]


class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsManager()]


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def manager_users(request):
    # Only an admin/superuser token can populate the Manager group (grading
    # criteria: "the admin can assign users to the manager group").
    if request.method == 'GET':
        managers = User.objects.filter(groups__name='Manager')
        return Response(UserSerializer(managers, many=True).data)

    username = request.data.get('username')
    if not username:
        return Response({'message': 'username is required'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)
    manager_group, _ = Group.objects.get_or_create(name='Manager')
    user.groups.add(manager_group)
    return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def manager_user(request, userId):
    user = get_object_or_404(User, pk=userId)
    if not user.groups.filter(name='Manager').exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.groups.remove(Group.objects.get(name='Manager'))
    return Response({'message': 'user removed from the manager group'})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsManager])
def delivery_crew_users(request):
    # Managers (not just admins) can populate the Delivery crew group.
    if request.method == 'GET':
        crew = User.objects.filter(groups__name='Delivery crew')
        return Response(UserSerializer(crew, many=True).data)

    username = request.data.get('username')
    if not username:
        return Response({'message': 'username is required'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)
    delivery_crew_group, _ = Group.objects.get_or_create(name='Delivery crew')
    user.groups.add(delivery_crew_group)
    return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsManager])
def delivery_crew_user(request, userId):
    user = get_object_or_404(User, pk=userId)
    if not user.groups.filter(name='Delivery crew').exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.groups.remove(Group.objects.get(name='Delivery crew'))
    return Response({'message': 'user removed from the delivery crew group'})


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        menuitem = serializer.validated_data['menuitem']
        quantity = serializer.validated_data['quantity']
        # unit_price/price are derived server-side from the menu item, never trusted from the client
        serializer.save(user=self.request.user, unit_price=menuitem.price, price=menuitem.price * quantity)

    def delete(self, request, *args, **kwargs):
        Cart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)


class OrdersView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status']  # ?status=true / ?status=false
    ordering_fields = ['date', 'total']

    def get_queryset(self):
        user = self.request.user
        if is_manager(user):
            return Order.objects.all()
        if user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=user)
        return Order.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        # Only customers place orders; they're built from that customer's current cart.
        if is_manager(request.user) or request.user.groups.filter(name='Delivery crew').exists():
            return Response(status=status.HTTP_403_FORBIDDEN)

        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({'message': 'cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        total = sum(item.price for item in cart_items)
        order = Order.objects.create(user=request.user, total=total)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                menuitem=item.menuitem,
                quantity=item.quantity,
                unit_price=item.unit_price,
                price=item.price,
            )
        cart_items.delete()  # empty the cart now that its items have moved to the order
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order = get_object_or_404(Order, pk=self.kwargs['pk'])
        user = self.request.user
        is_assigned_crew = order.delivery_crew_id == user.id

        # Owner, any manager, or the delivery crew member assigned to it can see the order;
        # everyone else gets a 404 instead of confirming the order exists.
        if order.user_id == user.id or is_manager(user) or is_assigned_crew:
            return order
        raise NotFound()

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        user = request.user
        is_assigned_crew = order.delivery_crew_id == user.id

        if is_manager(user):
            # A manager can reassign the delivery crew and/or flip the delivered status.
            serializer = self.get_serializer(order, data=request.data, partial=True)
        elif is_assigned_crew:
            # Delivery crew may only update `status`, nothing else on the order.
            serializer = self.get_serializer(order, data={'status': request.data.get('status')}, partial=True)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        if not is_manager(request.user):
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
