# Generated by Django 3.2.9 on 2021-12-05 16:07

import addproject.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0005_auto_20211204_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='picture',
            field=models.ImageField(default=1, upload_to=addproject.models.image_upload),
            preserve_default=False,
        ),
    ]