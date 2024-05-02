# Generated by Django 5.0.3 on 2024-04-29 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopping", "0005_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/userprofiles/"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="venmo_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
