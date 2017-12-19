from django.contrib import admin

from .models import Point

class PointAdmin(admin.ModelAdmin):
    list_display = ['user', 'admin', 'reason', 'end_point']
    search_fields = ['user', 'admin', 'reason', 'end_point']
    list_filter = ['user', 'admin', 'reason', 'end_point']


admin.site.register(Point, PointAdmin)
