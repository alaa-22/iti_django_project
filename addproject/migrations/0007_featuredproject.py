# Generated by Django 3.2.9 on 2021-12-02 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0006_alter_project_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_featured', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_project', to='addproject.project')),
            ],
        ),
    ]
