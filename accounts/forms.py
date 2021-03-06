from django import forms
from .models import Account
from django.contrib.auth import forms as auth_forms


class AccountCreationForm(auth_forms.UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required!')
        return email


class SignInForm(forms.Form):
    email = forms.CharField(max_length=60, widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


class ChangeUserInfo(auth_forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = "Change Profile Image"

    password = None

    class Meta:
        model = Account
        fields = ['image', 'username', 'email', 'first_name', 'last_name', 'bio', 'mobile_number']
        widgets = {'image': forms.FileInput()}
