from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account


class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Include all the required fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the user, but replaces  the password field
    with admin's password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('image', 'username', 'email', 'first_name', 'last_name', 'mobile_number', 'bio')
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def clean_password(self):
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    @staticmethod
    def Name(obj):
        return str(obj)

    list_display = ('Name', 'email', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'date_joined', 'last_login')
    ordering = ('-date_joined',)
    search_fields = ('username', 'email', 'mobile_number')
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('image', 'username', 'email', 'password')}),
        ("Personal info", {
            'fields':
                ('first_name',
                 'last_name',
                 'bio',
                 'mobile_number',
                 )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
                }),
    )


admin.site.register(Account, UserAdmin)
admin.site.unregister(Group)
