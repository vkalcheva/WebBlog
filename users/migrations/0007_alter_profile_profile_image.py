# Generated by Django 4.1.3 on 2022-11-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_profile_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="profiles/default.jpg",
                null=True,
                upload_to="profiles/",
            ),
        ),
    ]