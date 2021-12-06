# Generated by Django 3.2.9 on 2021-12-06 09:25

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to=accounts.models.image_upload)),
                ('phone', models.CharField(blank=True, max_length=15, validators=[accounts.models.phone_validator])),
                ('Birthdate', models.CharField(blank=True, max_length=30)),
                ('facebook_link', models.URLField(blank=True)),
                ('country', models.CharField(blank=True, choices=[('Egypt', 'Egypt'), ('Saudi Arabia', 'Saudi Arabia'), ('Sudan', 'Sudan'), ('Tunisia', 'Tunisia'), ('Algeria', 'Algeria'), ('Libya', 'Libya')], max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
