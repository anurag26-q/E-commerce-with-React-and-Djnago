# Generated by Django 5.0.6 on 2024-06-13 14:40

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, default='default/default.jpg', null=True, upload_to='image')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg', length=10, max_length=20, prefix='', unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauths.user')),
            ],
        ),
    ]
