from rest_framework import serializers

from .models import Contact, MyContact


class ContactFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class MyContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyContact
        fields = "__all__"
