from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Store)

admin.site.register(Store_location)

admin.site.register(Category)

admin.site.register(Videogame)

admin.site.register(Format)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Platform)
admin.site.register(Dlc)
admin.site.register(Shopping_cart_packages)
admin.site.register(Shopping_cart)
admin.site.register(Shopping_cart_videogames)
admin.site.register(Shopping_cart_dlc)

admin.site.register(Dispatcher)
admin.site.register(Package)