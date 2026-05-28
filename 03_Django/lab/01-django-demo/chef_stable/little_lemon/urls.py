from django.urls import path

from . import views


urlpatterns = [
    path("hello/", views.hello, name="little_lemon_hello"),
    path("menu/<int:item_id>/", views.menu_item, name="little_lemon_menu_item"),
    path("menu-card/<int:item_id>/", views.menu_card, name="little_lemon_menu_card"),
]
