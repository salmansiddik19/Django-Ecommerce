from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    CHOICES = (
        ('Owner', 'Owner'),
        ('Customer', 'Customer'),
    )

    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_category = models.CharField(
        max_length=10, choices=CHOICES, default='Customer')
    user_info = models.FileField(blank=True, null=True, upload_to='files/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_category']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
