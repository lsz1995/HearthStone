from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth import get_user_model,authenticate
from .serializers import UserRegSerializer,UserDetailSerializer,UserUpDataSerializer
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# from .models import RechargeOrder,WithdrawOrder,Store
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import serializers
# from .filters import WithdrawOrderFilter,RechargeOrderFilter
User =get_user_model()
# Create your views here.


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            print(password)
            a =user.check_password(password)
            print(a)

            # user_is = authenticate(username=username, password=password)
            if user.check_password(password):



                return user
        except Exception as e:

            return None

class GoodstPagination(PageNumberPagination):
    """
    配置分页情况
    """
    page_size = 10
    page_size_query_param = 'page_size'
    # page_query_param = "p"
    max_page_size = 100
class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):#UpdateModelMixin 修改
    """
    create:
        注册用户
    retrieve:
        用户详情
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all().order_by('id')#


    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )#用户认证方式

    def get_serializer_class(self):#选择序列化方式
        if self.action == "retrieve":
            return UserDetailSerializer#用户详情
        elif self.action == "create":
            return UserRegSerializer#用户注册

        return UserUpDataSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):#动态获取用户权限   注册的时候不需要登入状态    获取详情的时候需要登入状态
        if self.action == "retrieve":#获取详情  user/id
            return [permissions.IsAuthenticated()]
        elif self.action == "create":#注册
            return []

        return []

    def create(self, request, *args, **kwargs):#注册直接登入   重载
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user#返回当前用户

    def perform_create(self, serializer):
        return serializer.save()


from datetime import datetime
import time



