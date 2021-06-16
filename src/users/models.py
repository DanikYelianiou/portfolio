from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    avatar = models.ImageField(upload_to="users/avatar/", blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)