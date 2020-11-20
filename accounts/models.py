from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):
    pass


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('Username'),
        max_length=30,
        unique=True,
        blank=False,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        _('Email'),
        blank=False,
        max_length=60,
        unique=True
    )

    first_name = models.CharField(
        _('First name'),
        max_length=30,
        blank=True,
        default='John',
    )

    last_name = models.CharField(
        _('Last name'),
        max_length=30,
        blank=True,
        default='Doe'
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date joined'
    )

    bio = models.CharField(
        _('About'),
        max_length=1000,
        blank=True
    )

    image = models.ImageField(
        _('Image'),
        upload_to='users/profile_images/',
        default='users/no_profile_image.jpeg'
    )

    last_login = models.DateTimeField(
        auto_now=True,
        verbose_name='Last login'
    )

    is_superuser = models.BooleanField(default=False, verbose_name='Superuser')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')

    objects = AccountManager()
