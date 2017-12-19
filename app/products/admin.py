from django.contrib import admin

from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'point', 'ku_cun']
    search_fields = ['name', 'price', 'point', 'ku_cun']
    list_filter = ['name', 'price', 'point', 'ku_cun']










admin.site.register(Product,ProductAdmin)

