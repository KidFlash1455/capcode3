from .models import Survey
from django import forms


class CustomSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = (
            "first_name",
            "last_name",
            "suffix",
            "email",
            "status",
            "status_desc",
        )
