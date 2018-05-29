from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=true)
    #
    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name','email_address','password1','password2')