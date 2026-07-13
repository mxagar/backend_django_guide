from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.MenuItemDetailView.as_view()),
    path('groups/manager/users', views.manager_users),
    path('groups/manager/users/<int:userId>', views.manager_user),
    path('groups/delivery-crew/users', views.delivery_crew_users),
    path('groups/delivery-crew/users/<int:userId>', views.delivery_crew_user),
    path('cart/menu-items', views.CartView.as_view()),
    path('orders', views.OrdersView.as_view()),
    path('orders/<int:pk>', views.OrderDetailView.as_view()),
]
