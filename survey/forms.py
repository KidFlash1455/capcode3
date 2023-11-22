from .models import Survey
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class CustomSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        exclude = ("account",)
