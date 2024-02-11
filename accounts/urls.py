from django.urls import path, include
from django.contrib.auth import urls
from .views import SignupPageView

urlpatterns = [
    path("", include(urls)),
    path("signup/", SignupPageView.as_view(), name="signup")
]