# Generated by Django 5.0.6 on 2024-06-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0008_profile_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='otp',
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
