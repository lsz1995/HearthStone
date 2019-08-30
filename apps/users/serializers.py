# -*- coding:utf-8 -*-
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator

from django.db.models import Q


User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):##获取详情
    """
    用户详情序列化类
    """
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    date_joined = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = User
        fields = ("id",'user',"username", "qq_number", "email", "mobile",'user_type','date_joined')




class UserUpDataSerializer(serializers.ModelSerializer):#修改密码
    """
    用户修改密码序列化类
    """
    user = serializers.HiddenField(#
        default=serializers.CurrentUserDefault()
    )
    password = serializers.CharField(
        style={'input_type': 'password'},help_text="密码", label="密码",write_only=True,min_length=5,max_length=20,error_messages={
                                         "max_length": "密码长度应小于等于20",
                                         "min_length": "密码长度应大于等于5"}  #style  设置密码密文  write_only  序列化就不会带上password
    )
    old_password = serializers.CharField(
        style={'input_type': 'password'},help_text="旧密码", label="旧密码",write_only=True,min_length=5,max_length=20,error_messages={
                                         "max_length": "密码长度应小于等于20",
                                         "min_length": "密码长度应大于等于5"}  #style  设置密码密文  write_only  序列化就不会带上password
    )

    def validate_old_password(self, old_password):#验证过程

        a = self.instance.check_password(old_password)

        if a:
            pass
        else:

            raise serializers.ValidationError("旧密码错误")





    def update(self, instance, validated_data):#更新过程


        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        password = validated_data['password']
        instance.set_password(password)
        instance.save()

        return instance



    class Meta:
        model = User
        fields = ('user',"id",'password','old_password')









class UserRegSerializer(serializers.ModelSerializer):#    ModelSerializer    注册
    password = serializers.CharField(
        style={'input_type': 'password'},help_text="密码", label="密码",write_only=True,min_length=5, max_length=10,                                     error_messages={
                                         "max_length": "密码长度应小于等于20",
                                         "min_length": "密码长度应大于等于5"},  #style  设置密码密文  write_only  序列化就不会带上password
    )

    username = serializers.CharField(min_length=5, max_length=20,
                                     error_messages={
                                         "max_length": "用户名长度应小于等于20",
                                         "min_length": "用户名长度应大于等于5"},
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户名已经被使用')],
                                     help_text="用户名")

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)# 创建用户
        user.set_password(validated_data["password"])
        user.save()
        return user


    # def validate_mobile(self, mobile):#验证过程
    #
    #
    #     mobile_records = User.objects.filter(mobile=mobile)
    #     if mobile_records:
    #
    #         raise serializers.ValidationError("电话号码已存在")

    def validate_user_type(self, user_type):  # 验证充值金额
        if user_type == 0:
            raise serializers.ValidationError("管理员账号不允许注册，请到后台添加")
        return user_type

    def validate(self, attrs):  # 验证充值金额



        mobile_records = User.objects.filter(mobile=attrs['mobile'])
        if mobile_records:

            raise serializers.ValidationError("电话号码已存在")

        # user_records = User.objects.filter(username=attrs['username'])
        #
        # if user_records:
        #
        #     raise serializers.ValidationError("用户已存在")

        return attrs


    class Meta:
        model = User
        # fields = ("username", "code",'mobile',"password")
        fields = ("username", "mobile","password",'email','qq_number','user_type')


