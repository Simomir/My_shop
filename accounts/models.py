from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_delete
from django.dispatch import receiver


class AccountManager(BaseUserManager):
    def _create_user(self, email, username, password=None):
        """
        Creates a user with the given username, email and password.
        """
        if not email:
            raise ValueError("Users must provide an email address.")
        if not username:
            raise ValueError("Users must have a username.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password=None):
        user = self._create_user(email=email, username=username, password=password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


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
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists.')
        }
    )

    first_name = models.CharField(
        _('First name'),
        max_length=30,
        blank=True,
    )

    last_name = models.CharField(
        _('Last name'),
        max_length=30,
        blank=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date joined'
    )

    bio = models.CharField(
        _('About'),
        max_length=1000,
        blank=True,
    )

    image = models.ImageField(
        _('Image'),
        upload_to='users/profile_images/',
        default='users/no_profile_image.jpeg'
    )

    mobile_number = models.CharField(
        _('Mobile number'),
        max_length=10,
        blank=True,
    )

    last_login = models.DateTimeField(
        auto_now=True,
        verbose_name='Last login'
    )

    is_superuser = models.BooleanField(default=False, verbose_name='Superuser')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        db_table = 'auth_user'


# Delete the image (if there is one different than the default one)
# associated with the account on deletion of the account itself
@receiver(post_delete, sender=Account)
def submission_delete(sender, instance, **kwargs):
    if 'profile_images' in instance.image.url:
        instance.image.delete(False)
