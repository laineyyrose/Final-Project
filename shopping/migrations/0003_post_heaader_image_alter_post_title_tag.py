# Generated by Django 5.0.3 on 2024-04-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopping", "0002_post_title_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="heaader_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title_tag",
            field=models.CharField(max_length=255),
        ),
    ]
