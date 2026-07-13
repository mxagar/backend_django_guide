from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Cart, Category, MenuItem, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    # Split read/write: `category` nests the full object for GET responses,
    # `category_id` is the plain FK id accepted on POST/PUT/PATCH.
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CartSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), source='menuitem', write_only=True
    )
    # unit_price/price are computed from the menu item's price in the view, not sent by the client
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'menuitem', 'menuitem_id', 'quantity', 'unit_price', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'menuitem', 'quantity', 'unit_price', 'price']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    delivery_crew = serializers.PrimaryKeyRelatedField(read_only=True)
    # Managers assign delivery crew by id; only users in the Delivery crew group are valid targets
    delivery_crew_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(groups__name='Delivery crew'),
        source='delivery_crew',
        write_only=True,
        required=False,
    )
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'delivery_crew_id', 'status', 'total', 'date', 'items']
        read_only_fields = ['total', 'date']
