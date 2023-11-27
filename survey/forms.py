from .models import Survey
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper


class CustomSurveyForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["status"].widget.attrs.update(
    #         {
    #             "hx-get": reverse_lazy("survey_new"),
    #         }
    #     )
    #     self.helper = FormHelper(self)

    class Meta:
        model = Survey
        exclude = ("account",)
        help_texts = {
            "email": ".edu",
            "suffix": "e.g. John Smith, PHD, MD",
            "ds_class_1": "e.g. ABC 123 Advanced Data Science",
        }
