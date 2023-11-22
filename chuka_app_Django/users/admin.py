from django.contrib import admin

from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "email"]


admin.site.register(UserAccount, UserAccountAdmin)
