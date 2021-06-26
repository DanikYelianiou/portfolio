from rest_framework import generics

from .models import Resume
from .serializers import ResumeSerializer


class ResumeView(generics.ListAPIView):

    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
