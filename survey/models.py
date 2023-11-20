from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
STATUS_CHOICES = (
    ("Full-Time", "Full-Time"),
    ("Part-Time", "Part-Time"),
)


class Survey(models.Model):
    first_name = models.CharField(max_length=100, default="Default")
    last_name = models.CharField(max_length=100, default="Default")
    suffix = models.CharField(
        "Full Name including degrees/designations to be listed on web-site and directory:",
        max_length=100,
        default="Default",
    )
    email = models.EmailField(default="Default@default.com")
    status = models.CharField(
        "What is your status at the Marquette or UW-Milwaukee?",
        max_length=100,
        choices=STATUS_CHOICES,
    )
    status_desc = models.TextField(max_length=500, default="Default")
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

    def get_absolute_url(self):
        return reverse("survey_detail", kwargs={"pk": self.pk})
