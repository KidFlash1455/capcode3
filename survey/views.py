from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import FileResponse
import csv
import io

from .models import Survey
from .forms import CustomSurveyForm
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.


class SurveyListView(LoginRequiredMixin, ListView):
    model = Survey
    template_name = "survey_list.html"

    def get_queryset(self):
        return Survey.objects.filter(account=self.request.user)


class SurveyDetailView(LoginRequiredMixin, DetailView):
    model = Survey
    template_name = "survey_detail.html"


class SurveyUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Survey
    form_class = CustomSurveyForm
    template_name = "survey_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.account == self.request.user


class SurveyDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Survey
    template_name = "survey_delete.html"
    success_url = reverse_lazy("survey_list")

    def test_func(self):
        obj = self.get_object()
        return obj.account == self.request.user


class SurveyCreateView(LoginRequiredMixin, CreateView):
    form_class = CustomSurveyForm
    template_name = "survey_new.html"

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


# PDF File Generation
def survey_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    surveys = Survey.objects.all()
    lines = []

    for survey in surveys:
        lines.append(survey.first_name)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="survey.pdf")
