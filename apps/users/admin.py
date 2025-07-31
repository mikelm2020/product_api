from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_active", "is_staff")
    search_fields = ("username",)
    ordering = ("username",)
    list_filter = ("is_active", "is_staff")
