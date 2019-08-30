from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse,JsonResponse
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from rest_framework import mixins
from rest_framework import viewsets, filters
from .serializers import AllCardSerializer,AllCardGroupSerializer,Card_duikangSerializer,Card_pctSerializer,Deck_infoSerializer,Deck_hit_infoSerializer,Player_classSerializer,CardSerializer,CardGroupSerializer,Deck_info_DetailSerializer
from .filters import AllCard_filters,AllCardGroup_filters,Card_duikang_filters,Card_pct_filters,Deck_info_filters,Deck_hit_info_filters,Player_class_filters
from .models import ALL_cards,Card_group,Card_duikang,Card_pct,Deck_info,Deck_hit_info,Deck_Scheduling_info,Player_class
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import MySQLdb
import requests
import json
from unit.IPfuntion import getHtml
class GoodstPagination(PageNumberPagination):
    """
    配置分页情况
    """
    page_size = 500
    page_size_query_param = 'page_size'
    # page_query_param = "p"
    max_page_size = 100


class UpDataView(View):


    def get(self, request):
        # from cards.models import ALL_cards
        #
        # # get_cards_info()
        # # 更新卡牌信息， 新版本出了手动添加新版本
        # import json
        # with open("F:\HearthStone\data\cards.json", 'r', encoding='utf-8') as load_f:
        #     load_dict = json.load(load_f)
        # for i in load_dict:
        #
        #         try:
        #             id = i['dbfId']
        #         except:
        #             print('没有ID')
        #
        #         user_email = ALL_cards.objects.filter(card_dbf_id=id)
        #         # print(len(user_email))
        #         if len(user_email)!=0:
        #
        #             user_email[0].card_id = i['id']
        #
        #             user_email[0].card_name =i['name']
        #             user_email[0].card_en_name =i['artist']
        #             user_email[0].card_text =i.get('text','')
        #             user_email[0].card_type =i['type']
        #             user_email[0].card_rarity =i['rarity']
        #             user_email[0].card_cardClass =i['cardClass']
        #             user_email[0].card_cost =i['cost']
        #             if i['set'] in ['CORE','EXPERT1','DALARAN','TROLL','BOOMSDAY','GILNEAS']:
        #                 user_email[0].is_standard =True
        #
        #
        #             user_email[0].card_set =i['set']
        #             user_email[0].card_race =i.get('race','')
        #             user_email[0].card_mechanism =i.get('mechanics','')
        #             user_email[0].card_image ='https://art.hearthstonejson.com/v1/tiles/{}.png'.format(i['id'])
        #             user_email[0].card_min_image ='https://art.hearthstonejson.com/v1/render/latest/zhCN/512x/{}.png'.format(i['id'])
        #             user_email[0].save()
        #             print(user_email[0].card_name)
        #             print('保存')
        # # 更新卡牌信息， 新版本出了手动添加新版本

        from .Class_UpData import LUSHI_UPDATA
        from .Class_UpData import LUSHI_UPDATA
        UP = LUSHI_UPDATA()
        # UP.UP_DATA_CARDS()#获取当前环境下所有狂野环境的卡牌ID,   新版本更新一次
        # UP.UP_CARDS_INFO()#更新卡牌基本信息， 用最新的    card.json 新版本更新一次

        UP.UP_DATA_EVERY_DAY()  # 更新每天的卡牌胜率   每天一次
        # UP.UPDATA_GROUP_all()  # 更新所有卡组原型   有的更新 ，没有的跳过
        # UP.GetGroup_pct_info()  # 更新卡组原型情况
        # UP.Get_head_to_head_archetype_matchups()  # 卡组原型对抗情况 需要删除旧的
        # UP.Get_Player_class()  # 更新职业对抗
        # UP.UP_Decks()  # 更新套牌
        # UP.Get_Deck_hit_info()
        # 更新套牌对抗信息
        print('更新完毕')



        return HttpResponse('申请的更新已经成功')


class AllCardViewset(mixins.ListModelMixin, viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    queryset = ALL_cards.objects.all()
    serializer_class = AllCardSerializer
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AllCard_filters
    search_fields = ('card_name',)

    def get_serializer_class(self):#选择序列化方式
        if self.action == "retrieve":
            return CardSerializer#卡牌详情

        return AllCardSerializer

    def retrieve(self, request, *args, **kwargs):

        # instance = self.get_object()

        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        instance = ALL_cards.objects.get(card_dbf_id=filter_kwargs['pk'])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)






#原型
class AllCardGroupViewset(mixins.ListModelMixin, viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    queryset = Card_group.objects.all()
    serializer_class = AllCardGroupSerializer
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AllCardGroup_filters
    search_fields = ('Group_name',)


    def get_serializer_class(self):#选择序列化方式
        if self.action == "retrieve":
            return CardGroupSerializer#卡牌详情

        return AllCardGroupSerializer

    def retrieve(self, request, *args, **kwargs):

        # instance = self.get_object()

        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        instance = Card_group.objects.get(Group_id=filter_kwargs['pk'])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Card_duikangViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    #原型对抗
    queryset = Card_duikang.objects.all()
    serializer_class = Card_duikangSerializer
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = Card_duikang_filters
    search_fields = ('Group_id',)






class Card_pctViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    #原型占比
    queryset = Card_pct.objects.all()
    serializer_class = Card_pctSerializer
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = Card_pct_filters
    search_fields = ('Group_id',)




class Deck_infoViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    #原型占比
    queryset = Deck_info.objects.all()
    serializer_class = Deck_infoSerializer
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = Deck_info_filters
    search_fields = ('Deck_archetype_id',)

    def get_serializer_class(self):#选择序列化方式
        if self.action == "retrieve":
            return Deck_info_DetailSerializer#卡牌详情

        return Deck_infoSerializer
    def retrieve(self, request, *args, **kwargs):

        # instance = self.get_object()

        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        instance = Deck_info.objects.get(Deck_deck_id=filter_kwargs['pk'])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)




class Deck_hit_infoViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    #原型占比
    queryset = Deck_hit_info.objects.all()
    serializer_class = Deck_hit_infoSerializer
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = Deck_hit_info_filters
    search_fields = ('Deck_deck_id',)
class Player_classViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    #原型占比
    queryset = Player_class.objects.all()
    serializer_class = Player_classSerializer
    pagination_class = GoodstPagination  # 配置分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = Player_class_filters
    search_fields = ('zhiye',)





from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

try:
    print('启动定时器')
    # 实例化调度器
    scheduler = BackgroundScheduler()
    # 调度器使用DjangoJobStore()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # 设置定时任务，选择方式为interval，时间间隔为10s
    # 另一种方式为每天固定时间执行任务，对应代码为：
    import datetime
    @register_job(scheduler, 'cron', day_of_week='mon-fri', hour='02', minute='00', second='00',id='UpData')
    # @register_job(scheduler,"interval", seconds=10)
    def my_job():
        from .Class_UpData import LUSHI_UPDATA
        print(datetime.datetime.now(),'开始')
        UP = LUSHI_UPDATA()
        # UP.UP_DATA_CARDS()#获取当前环境下所有狂野环境的卡牌ID,   新版本更新一次
        # UP.UP_CARDS_INFO()#更新卡牌基本信息， 用最新的    card.json 新版本更新一次

        UP.UP_DATA_EVERY_DAY()  # 更新每天的卡牌胜率   每天一次
        UP.UPDATA_GROUP_all()  # 更新所有卡组原型   有的更新 ，没有的跳过
        UP.GetGroup_pct_info()  # 更新卡组原型情况
        UP.Get_head_to_head_archetype_matchups()  # 卡组原型对抗情况 需要删除旧的

        UP.Get_Player_class()  # 更新职业对抗
        UP.UP_Decks()  # 更新套牌
        UP.Get_Deck_hit_info()  # 更新套牌对抗信息
        print('更新完毕')
        print(datetime.datetime.now())



        # UpData()
#         pass
    register_events(scheduler)
    scheduler.start()



except Exception as e:
    print(e)
    # 有错误就停止定时器
    scheduler.shutdown()


