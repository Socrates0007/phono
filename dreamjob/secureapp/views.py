from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SignupForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
class SignupView(CreateView):
    form_class=SignupForm
    template_name='secureapp/signup.html'
    success_url=reverse_lazy('homepage')