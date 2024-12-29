# Generated by Django 5.1.2 on 2024-12-29 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]