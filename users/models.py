import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, role='client', **extras_fields):
        if not email:
            raise ValueError('The email is required and cannot be blank.')
        if not password:
            raise ValueError('The password is required and cannot be blank.')
        user = self.model(username=username, email=email,
                          role=role, **extras_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extras_fields):

        extras_fields.setdefault('is_staff', True)
        extras_fields.setdefault('is_superuser', True)
        return self.create_user(username=username, email=email, password=password, role='admin', **extras_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.

    Inherited fields:
        - password: secure hashed password (inherited from AbstractBaseUser).
        - last_login: date of the last login (inherited from AbstractBaseUser).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    # The password comes from AbstractBaseUser and is already stored with a hash.
    ROLE_CHOICES = [('client', 'Client'), ('admin', 'Administrator')]
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='client')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        default=False, help_text='Designates whether the user can log into this admin site.')
    date_joined = models.DateField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} - {self.email}'
