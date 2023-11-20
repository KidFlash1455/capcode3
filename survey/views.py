from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Survey
from .forms import CustomSurveyForm

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
    fields = (
        "first_name",
        "last_name",
        "suffix",
        "email",
        "status",
        "status_desc",
    )
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
