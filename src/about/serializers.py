from rest_framework import serializers

from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):

    github = serializers.SlugRelatedField(slug_field="link", read_only=True)
    hard_skills = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    extra_skills = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    soft_skills = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    english_lvls = serializers.SlugRelatedField(slug_field="english_lvl", read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"
