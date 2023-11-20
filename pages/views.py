from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from survey.models import Survey

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


@login_required
def get_home(request):
    try:
        Survey.objects.get(account=request.user.id)
        return render(request, "home.html")
    except ObjectDoesNotExist:
        return render(request, "home_newuser.html")
