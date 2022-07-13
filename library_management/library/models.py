from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    user_name = models.CharField(max_length=255,null=False)
    password = models.CharField(max_length=255,null=False)
    email_id = models.CharField(max_length=255,null=False)

    REQUIRED_FIELDS = []

