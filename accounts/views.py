from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("index")
    template_name = "registration/signup.html"
