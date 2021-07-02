from rest_framework import generics, permissions

from .models import Contact, MyContact
from .serializers import ContactFormSerializer, MyContactSerializer


class ContactCreateView(generics.CreateAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MyContactView(generics.ListAPIView):

    queryset = MyContact.objects.all()
    serializer_class = MyContactSerializer
