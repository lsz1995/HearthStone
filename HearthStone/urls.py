"""HearthStone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin


from django.views.static import serve

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from HearthStone.settings import MEDIA_ROOT
from users.views import UserViewset
from .settings import STATIC_ROOT
# from operation.views import AnnouncementViewset,TaskPriceViewset,GetPicViewset
from cards.views import UpDataView,AllCardViewset,AllCardGroupViewset,Card_duikangViewset,Card_pctViewset,Deck_infoViewset,Deck_hit_infoViewset,Player_classViewset
# from apps.task.views import BrushTaskViewset,AllBrushTaskViewset,MyTaskViewset,MyTaskOrderViewset,LogisticsTaskViewset
router = DefaultRouter()
router.register(r'users', UserViewset, base_name="users")
router.register(r'AllCard', AllCardViewset, base_name="Recharge")#所有卡牌
router.register(r'AllCardGroup', AllCardGroupViewset, base_name="AllCardGroup")#所有原型
router.register(r'Grouphit', Card_duikangViewset, base_name="Grouphit")#所有原型
router.register(r'grouppct', Card_pctViewset, base_name="grouppct")#所有原型
router.register(r'Deck_info', Deck_infoViewset, base_name="Deck_info")#所有原型
router.register(r'Deck_hit_info', Deck_hit_infoViewset, base_name="Deck_hit_info")#所有原型
router.register(r'Player_class', Player_classViewset, base_name="Player_class")#所有原型


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),  # 后台管理
    url(r'^login/', obtain_jwt_token),  # 接收账号密码 生成token签名信息
    url(r'docs/', include_docs_urls(title="炉石传说")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'^GetPic/$', GetPicViewset.as_view(), name='GetPic'),
    url(r'^test/', UpDataView.as_view(), name='UploadVideo'),#  测试功能
    url(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}, name='static')#部署用
#

]
