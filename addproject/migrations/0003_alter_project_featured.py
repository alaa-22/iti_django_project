# Generated by Django 3.2.9 on 2021-12-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0002_project_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]