# -*- coding: utf-8 -*-
import pytz
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers

from models import Reg, Group, Member

utc_tz = pytz.timezone('UTC')

Users = get_user_model()

class RegSer(serializers.ModelSerializer):
    class Meta:
        model = Reg
        fields = '__all__'

    def validate(self, attrs):
        instance = Reg.objects.filter(mobile=attrs['mobile']).order_by('-add_time')
        if instance:  # update method
            now = datetime.now().replace(tzinfo=utc_tz)
            if 'password' not in attrs.keys():  # 更新验证码
                if now -timedelta(hours=8, seconds=60) < instance[0].add_time:
                    raise serializers.ValidationError('间隔时间过短')
            else:   # 注册
                if now - timedelta(hours=8, minutes=5) > instance[0].add_time:
                    raise serializers.ValidationError('验证码已过期')
                if attrs['code'].encode() != instance[0].code:
                    raise serializers.ValidationError('验证码错误')
            return attrs
        return attrs  # create method


class UserReg(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    id = serializers.IntegerField(read_only=True, required=False)
    date_joined = serializers.DateTimeField(required=False)

    class Meta:
        model = Users
        fields = ('id','username', 'password', 'date_joined')


class GroupSer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class MemberSer(serializers.ModelSerializer):
    group = GroupSer()
    class Meta:
        model = Member
        fields = '__all__'


class GroupContenSer(serializers.ModelSerializer):
    group_category = MemberSer(many=True,read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'group_category')