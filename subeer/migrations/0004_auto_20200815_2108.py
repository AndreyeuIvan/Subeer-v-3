# Generated by Django 3.1 on 2020-08-15 21:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("subeer", "0003_auto_20200813_2238"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episode",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 15, 21, 8, 0, 692782, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 15, 21, 8, 0, 692809, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="serial",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 15, 21, 8, 0, 692165, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="serial",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 15, 21, 8, 0, 692199, tzinfo=utc)
            ),
        ),
    ]
