from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(("Email"), max_length=254, unique=True)
    # chat=models.CharField(max_length=20)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('staff'), default=False)
    is_superuser = models.BooleanField(('superuser'), default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_email(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.email.strip()

