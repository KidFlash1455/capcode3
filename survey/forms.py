from .models import Survey
from django import forms


class CustomSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        exclude = ("account",)
