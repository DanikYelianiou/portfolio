from rest_framework import serializers

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ("title", "photo", "description")


class ProjectDetailSerializer(serializers.ModelSerializer):

    Technologies = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Project
        fields = "__all__"
