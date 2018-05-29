from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUp(generic.CreateView):
    from_class = UserCreationForm
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email= forms.EmailField(max_length=30, required=False, help_text='Optional')
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)