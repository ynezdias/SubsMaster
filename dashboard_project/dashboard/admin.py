from django.contrib import admin
from .models import Usermaster, Subscription

class UsermasterAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'f_name', 'l_name', 'is_active', 'expiry_date', 'activation_date', 'last_login', 'status']
    list_filter = ['is_active', 'status']
    search_fields = ['username', 'f_name', 'l_name']

admin.site.register(Usermaster, UsermasterAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['productname', 'user', 'act_date', 'end_date', 'is_active']
    list_filter = ['is_active']
    search_fields = ['user__username']

admin.site.register(Subscription, SubscriptionAdmin)
