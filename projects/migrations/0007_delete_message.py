# Generated by Django 4.1.3 on 2022-12-08 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0006_message"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Message",
        ),
    ]
