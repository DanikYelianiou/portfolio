from django.db import models

from src.users.models import CustomUser


class Technology(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"


class Project(models.Model):

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="projects/")
    description = models.TextField(max_length=5000)
    link = models.CharField(max_length=256)
    Technologies = models.ManyToManyField(Technology)
    ReadMe = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Comment(models.Model):

    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name="children")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
