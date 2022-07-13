from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ROLE_CHOICE = ((1, 'LIBRARIAN'),
                   (2, 'MEMBER'))
    user_name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    email_id = models.CharField(max_length=255, null=False)
    role = models.PositiveIntegerField(choices=ROLE_CHOICE, default=2)
    REQUIRED_FIELDS = []

