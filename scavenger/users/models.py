from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin


class UserManager(BaseUserManager):
    """Manager for custom user model."""

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""

    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    CASE_INSENSITIVE_FIELDS = ['email']

    def __str__(self):
        return '{}'.format(self.email)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return '{}'.format(self.first_name)

    def is_superuser(self):
        return self.is_staff

    def get_display_name(self):
        # 🤓 Ex: If email is 'abc1@students.uwf.edu', display name is 'abc1'
        return self.email.split('@')[0]
