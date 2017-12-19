from django.contrib import admin
from .models import UserProfile, Banner

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['sex', 'wechat_name', 'points', 'mobile', 'city']
    search_fields = ['wechat_name', 'sex', 'points', 'mobile', 'city']
    list_filter = ['wechat_name', 'sex', 'points', 'mobile', 'city']

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'add_time', 'index']
    search_fields = ['title', 'add_time', 'index']
    list_filter = ['title', 'add_time', 'index']

admin.site.register(Banner, BannerAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


