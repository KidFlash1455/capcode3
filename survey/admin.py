from django.contrib import admin
from .models import Survey


class CustomUserSurvey(admin.ModelAdmin):
    list_display = [
        "account",
        "first_name",
        "last_name",
        "email",
    ]


admin.site.register(Survey, CustomUserSurvey)
