from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    model = User
    add_fieldsets = UserAdmin.add_fieldsets 
    fieldsets = UserAdmin.fieldsets
    list_display = ('username', 'email', 'first_name', 'last_name')
