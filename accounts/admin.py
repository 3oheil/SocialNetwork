from django.contrib import admin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'country']


@admin.register(models.Country)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbr', 'is_active']
