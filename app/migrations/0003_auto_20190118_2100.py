# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-18 13:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190118_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
