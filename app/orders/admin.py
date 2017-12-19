from django.contrib import admin

from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'send_company', 'send_code']
    search_fields = ['user', 'product', 'send_company', 'send_code']
    list_filter = ['user', 'product', 'send_company', 'send_code']


admin.site.register(Orders, OrdersAdmin)