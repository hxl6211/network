# Generated by Django 3.1.3 on 2020-11-10 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20201110_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 0, 33, 24, 716268)),
        ),
    ]
