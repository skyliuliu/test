# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, filters, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.filters import SearchFilter

from models import Reg, Group, Member
from serializers import UserReg, RegSer, GroupSer, MemberSer, GroupContenSer

Users = get_user_model()

def index(request):
    return render(request, template_name='t.html')


class CacheView(APIView):
    @method_decorator(cache_page(10))
    def get(self,request):
        return Response('ok')

# Create your views here.
class UserViews(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserReg
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('username',)

    # def get_object(self):
    #     print dir(self.request.user)
    #     return self.request.user

    # def get_queryset(self):
    #     return Users.objects.filter(username=self.request.user.username) or self.queryset

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return []


class RegViews(viewsets.ModelViewSet):
    '''
    list:
        注册账号列表
    retrieve:
        按照手机号码现实注册账号
    create:
        发送验证码
    update:
        账号注册或者生成验证码
    delete:
        删除注册账号
    '''
    queryset = Reg.objects.all()
    serializer_class = RegSer
    lookup_field = 'mobile'


class GroupViews(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupContenSer

class MemberViews(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSer