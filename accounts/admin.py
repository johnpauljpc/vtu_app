from django.contrib import admin
from .models import User, UserProfile
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'phone_number','wallet_balance']

admin.site.register(User, CustomUserAdmin)

    

admin.site.register(UserProfile)