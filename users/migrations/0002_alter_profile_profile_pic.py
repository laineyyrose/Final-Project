# Generated by Django 5.0.3 on 2024-04-25 01:42

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                default="userprofiles/default.jpg",
                null=True,
                upload_to=users.models.Profile.user_directory_path,
            ),
        ),
    ]