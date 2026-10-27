from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "full_name",
        "phone",
        "area",
        "blood_group",
        "is_available",
        "is_volunteer",
        "is_donor",
        "is_repair_provider",
    )
    list_filter = ("is_available", "is_volunteer", "is_donor", "is_repair_provider", "blood_group")
    search_fields = ("user__username", "full_name", "phone", "area")

# Register your models here.
