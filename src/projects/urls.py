from django.urls import path

from .views import ProjectView, ProjectDetailView, CommentCreateView


urlpatterns = [
    path('projects/', ProjectView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),
    path('comments/', CommentCreateView.as_view()),
]
