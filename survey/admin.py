from django.contrib import admin
from .models import Survey


class CustomUserSurvey(admin.ModelAdmin):
    list_display = [
        "account",
        "get_active",
        "first_name",
        "last_name",
        "email",
    ]

    @admin.display(ordering="account__active", description="Active")
    def get_active(self, obj):
        return obj.account.active


admin.site.register(Survey, CustomUserSurvey)
