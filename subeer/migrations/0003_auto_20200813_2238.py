# Generated by Django 3.1 on 2020-08-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subeer", "0002_auto_20200808_1348"),
    ]

    operations = [
        migrations.AddField(
            model_name="episode",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="episode",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="episode",
            name="url",
            field=models.URLField(blank=True, max_length=133),
        ),
        migrations.AddField(
            model_name="serial",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="serial",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
