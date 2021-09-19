from django.contrib import admin

from .models import Product, WishList


admin.site.register(Product) #  можно наблюдать за продуктом из админки
admin.site.register(WishList)