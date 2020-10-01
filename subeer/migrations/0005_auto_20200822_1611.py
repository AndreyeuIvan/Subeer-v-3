# Generated by Django 3.1 on 2020-08-22 16:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subeer', '0004_auto_20200815_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='is_favorite',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1),
        ),
        migrations.AlterField(
            model_name='episode',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 16, 11, 49, 599300, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='episode',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 16, 11, 49, 599332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 16, 11, 49, 598207, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 16, 11, 49, 598240, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subeer.serial')),
            ],
        ),
    ]