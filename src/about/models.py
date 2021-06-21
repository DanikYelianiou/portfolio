from django.db import models


class GitHub(models.Model):

    link = models.CharField(max_length=256)
    picture = models.ImageField(upload_to="links/")

    def __str__(self):
        return "Мой гит хаб"

    class Meta:
        verbose_name = "GitHub"
        verbose_name_plural = "GitHubs"


class HardSkill(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "HardSkill"
        verbose_name_plural = "HardSkills"


class ExtraSkill(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ExtraSkill"
        verbose_name_plural = "ExtraSkills"


class SoftSkill(models.Model):

    LEVEL = (
        ("A1", "Beginner"),
        ("A2", "Elementary"),
        ("B1", "Intermediate"),
        ("B2", "Upper intermediate"),
        ("C1", "Advanced"),
        ("C2", "Mastery"),
    )

    english_lvl = models.CharField(max_length=20, choices=LEVEL)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.english_lvl} and {self.name}"

    class Meta:
        verbose_name = "SoftSkill"
        verbose_name_plural = "SoftSkills"


class Resume(models.Model):

    first_name = models.CharField(max_length=6)
    last_name = models.CharField(max_length=10)
    age = models.DateField(auto_now=False, auto_now_add=False)
    avatar = models.ImageField(upload_to="users/avatar/")
    description = models.TextField(max_length=5000)
    github = models.OneToOneField(GitHub, null=True, on_delete=models.CASCADE)
    hard_skills = models.ManyToManyField(HardSkill)
    extra_skills = models.ManyToManyField(ExtraSkill)
    soft_skills = models.ManyToManyField(SoftSkill)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"
