from django.contrib import admin
from . import models


@admin.register(models.Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['request_from', 'request_to', 'create_date', 'is_accepted']
    actions = False

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
