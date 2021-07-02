from django.urls import path

from .views import ContactCreateView, MyContactView


urlpatterns = [
    path('contacts/', ContactCreateView.as_view()),
    path('contacts/', MyContactView.as_view()),
]
