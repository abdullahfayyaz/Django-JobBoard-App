from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    is_company = forms.BooleanField(required=False, label='Are you a company?')
    class Meta:
        model = User
        fields = ('username', 'email', 'is_company', 'password1', 'password2')