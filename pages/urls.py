from django.urls import path
from . import views
from .views import get_home

urlpatterns = [
    path("", views.get_home, name="home"),
]

# from django.urls import path
# from .views import HomePageView
# from . import views

# urlpatterns = [
#     path("", HomePageView.as_view(), name="home"),
# ]
