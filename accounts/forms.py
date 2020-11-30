from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']
