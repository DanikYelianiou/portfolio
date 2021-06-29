from rest_framework import serializers

from .models import Project, Comment


class FilterCommentListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ("title", "photo", "description")


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("name", "text", "children")



class ProjectDetailSerializer(serializers.ModelSerializer):

    Technologies = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"
