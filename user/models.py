from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    CHOICES = (
        ('owner', 'owner'),
        ('customer', 'customer'),
    )

    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_category = models.CharField(max_length=10, choices=CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_category']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email
