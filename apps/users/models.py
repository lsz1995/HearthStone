from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class UserProfile(AbstractUser):#扩展原有user表  setting注册加 AUTH_USER_MODEL='users.UserProfile'
    USER_CHOICES = (
        (0, "管理员"),
        (1, "卖家"),
        (2, "刷手"),
        (3, "代理"),
    )
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名",help_text='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月",help_text='出生年月')
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别",help_text='性别')
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话",help_text='电话')
    # my_email = models.EmailField(max_length=110, null=True, blank=True, verbose_name="邮箱")
    qq_number =models.CharField(null=True,blank=True,max_length=15,verbose_name='QQ号码',help_text='qq号码')
    # balance = models.FloatField(null=True,verbose_name='余额',default=0,help_text='余额',max_digits = 10, decimal_places = 2)
    # balance = models.DecimalField(null=True,verbose_name='余额',default=0,help_text='余额',max_digits = 10, decimal_places = 2)
    user_type = models.IntegerField(default=1, choices=USER_CHOICES, verbose_name="账号类别",
                                      help_text=u"账号类别: 0(管理员),1(卖家),2(刷手),3(代理)")
    # Invite_code = models.CharField(default='', blank=True,max_length=8,verbose_name=u'个人邀请码',help_text='个人邀请码 用来给别人填 代表是被次账号邀请')
    # Be_Invite_code = models.CharField(default='', blank=True,max_length=8,verbose_name=u'被邀请码',help_text='被邀请人的邀请码')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
    def get_activity(self):
        return self.brushtask_set.all()