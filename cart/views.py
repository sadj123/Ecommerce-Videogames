from django.shortcuts import render, redirect
from gde.models import *
from django.contrib.auth.decorators import login_required
from gde.decorators import allowed_users
from .cart import Cart

# Create your views here.

@login_required
@allowed_users(allowed_roles= ['Store'])
def add_videogame(request, videogame_name):
    cart = Cart(request)
    videogame = Videogame.objects.get(videogame_name=videogame_name)
    cart.add_videogame(videogame = videogame)
    return redirect("list_videogame")

@login_required
@allowed_users(allowed_roles= ['Store'])
def add_dlc(request, dlc_name):
    cart = Cart(request)
    dlc = Dlc.objects.get(dlc_name = dlc_name )
    cart.add_dlc(dlc = dlc)
    return redirect("list_dlc_dic")

@login_required
@allowed_users(allowed_roles= ['Store'])
def add_package(request, package_name):
    cart = Cart(request)
    package = Package.objects.get(package_name=package_name)
    cart.add_package(package = package)
    return redirect("list_package")

@login_required
@allowed_users(allowed_roles= ['Store'])
def remove_videogame(request, videogame_name):
    cart = Cart(request)
    videogame = Videogame.objects.get(videogame_name=videogame_name)
    cart.remove_videogame(videogame = videogame)
    return redirect("list_videogame")

@login_required
@allowed_users(allowed_roles= ['Store'])
def remove_dlc(request, dlc_name):
    cart = Cart(request)
    dlc = Dlc.objects.get(dlc_name=dlc_name)
    cart.remove_dlc(dlc = dlc)
    return redirect("list_dlc_dic")

@login_required
@allowed_users(allowed_roles= ['Store'])
def remove_package(request, package_name):
    cart = Cart(request)
    package = Package.objects.get(package_name=package_name)
    cart.remove_package(package = package)
    return redirect("list_package")

@login_required
@allowed_users(allowed_roles= ['Store'])
def decrease_videogame(request, videogame_name):
    cart = Cart(request)
    videogame = Videogame.objects.get(videogame_name=videogame_name)
    cart.decrease_videogame(videogame=videogame)
    return redirect("list_videogame")

@login_required
@allowed_users(allowed_roles= ['Store'])
def decrease_dlc(request, dlc_name):
    cart = Cart(request)
    dlc = Dlc.objects.get(dlc_name=dlc_name)
    cart.decrease_dlc(dlc = dlc)
    return redirect("list_dlc_dic")

@login_required
@allowed_users(allowed_roles= ['Store'])
def decrease_package(request, package_name):
    cart = Cart(request)
    package = Package.objects.get(package_name=package_name)
    cart.decrease_package(package = package)
    return redirect("list_package")

@login_required
@allowed_users(allowed_roles= ['Store'])
def clear_cart_dlc(request):
    cart = Cart(request)
    cart.clear()
    return redirect("list_dlc_dic")

@login_required
@allowed_users(allowed_roles= ['Store'])
def clear_cart_videogame(request):
    cart = Cart(request)
    cart.clear()
    return redirect("list_videogame")

@login_required
@allowed_users(allowed_roles= ['Store'])
def clear_cart_package(request):
    cart = Cart(request)
    cart.clear()
    return redirect("list_package")