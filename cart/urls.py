from django.urls import path
from .views import *

app_name = "cart"

urlpatterns = [
    path('add_videogame/<str:videogame_name>/', add_videogame, name='add_videogame'),
    path('add_dlc/<str:dlc_name>/', add_dlc, name='add_dlc'),
    path('add_package/<str:package_name>/', add_package, name='add_package'),

    path('remove_videogame/<str:videogame_name>/', remove_videogame, name="remove_videogame"),
    path('remove_dlc/<str:dlc_name>/', remove_dlc, name="remove_dlc"),
    path('remove_package/<str:package_name>/', remove_package, name="remove_package"),

    path('decrease_videogame/<str:videogame_name>/', decrease_videogame , name="decrease_videogame"),
    path('decrease_dlc/<str:dlc_name>/', decrease_dlc , name="decrease_dlc"),
    path('decrease_package/<str:package_name>/', decrease_package , name="decrease_package"),

    path('clear_videogame/', clear_cart_videogame , name='clear_cart_videogame'),
    path('clear_dlc/', clear_cart_dlc , name='clear_cart_dlc'),
    path('clear_package/', clear_cart_package , name='clear_cart_package'),

    path('decrease_product/<str:product_name>/', decrease_cart, name= 'decrease_product'),
    path('increase_product/<str:product_name>/', increase_cart, name= 'increase_cart'),
]
