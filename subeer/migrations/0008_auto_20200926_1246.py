# Generated by Django 3.1 on 2020-09-26 12:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("subeer", "0007_auto_20200904_1814"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episode",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 9, 26, 12, 46, 17, 560633, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="episode",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 9, 26, 12, 46, 17, 560660, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="serial",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 9, 26, 12, 46, 17, 559435, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="serial",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 9, 26, 12, 46, 17, 559466, tzinfo=utc)
            ),
        ),
    ]
