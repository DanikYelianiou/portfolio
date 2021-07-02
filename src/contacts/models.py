from django.conf import settings
from django.db import models


class Contact(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    company = models.CharField(max_length=128)
    contact_text = models.TextField(max_length=1500)

    def __str__(self):
        return f"С вами связывается {self.user} из компании {self.company}"


class MyContact(models.Model):

    text = models.TextField(max_length=1000, null=True)
    main_email = models.CharField(max_length=100, default="danik04_02@mail.ru")
    main_phone = models.CharField(max_length=17, default="+375(44)728-74-39")
    vk = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
