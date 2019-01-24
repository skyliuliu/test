# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

Users = get_user_model()

class Reg(models.Model):
    username = models.CharField(max_length=20, unique=True, null=True, blank=True)
    password = models.CharField(max_length=60, null=True, blank=True)
    code = models.CharField(max_length=4)
    mobile = models.CharField(max_length=11, unique=True)
    add_time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.username or self.mobile

    class Meta:
        verbose_name = u'注册账号'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)


class Group(models.Model):
    group_name = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.group_name

    class Meta:
        verbose_name = '群组'
        verbose_name_plural = verbose_name


class Member(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    group = models.ForeignKey(Group, related_name='group_category',verbose_name='群组')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '成员'
        verbose_name_plural = verbose_name