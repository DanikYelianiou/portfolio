# Generated by Django 3.2.4 on 2021-06-21 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20210621_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_lvl', models.CharField(choices=[('Beginner', 'Beginner'), ('Elementary', 'Elementary'), ('Intermediate', 'Intermediate'), ('Upper intermediate', 'Upper intermediate'), ('Advanced', 'Advanced'), ('Mastery', 'Mastery')], max_length=20)),
            ],
            options={
                'verbose_name': 'EnglishLevel',
                'verbose_name_plural': 'EnglishLevels',
            },
        ),
        migrations.RemoveField(
            model_name='softskill',
            name='english_lvl',
        ),
        migrations.AddField(
            model_name='resume',
            name='english_lvl',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='about.english'),
        ),
    ]
