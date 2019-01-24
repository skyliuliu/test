# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-18 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=60, null=True)),
                ('code', models.CharField(max_length=4)),
                ('mobile', models.CharField(max_length=11, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('add_time',),
                'verbose_name': '\u6ce8\u518c\u8d26\u53f7',
                'verbose_name_plural': '\u6ce8\u518c\u8d26\u53f7',
            },
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('id',), 'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
    ]