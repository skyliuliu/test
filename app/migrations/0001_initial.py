# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-12 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='male', max_length=16)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]