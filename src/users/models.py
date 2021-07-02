from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    avatar = models.ImageField(upload_to="users/avatar/", blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.email)
