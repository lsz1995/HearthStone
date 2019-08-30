# -*- coding:utf-8 -*-
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator

from django.db.models import Q
from .models import ALL_cards,Card_group,Card_duikang,Card_pct,Deck_info,Deck_hit_info,Deck_Scheduling_info,Player_class
User = get_user_model()

#卡牌列表
class AllCardSerializer(serializers.ModelSerializer):##获取所有卡牌列表
    """
    公告序列化
    """
    updatetime = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = ALL_cards
        fields = ['id','card_dbf_id','card_id','card_name','card_image','card_min_image','card_winrate_play_out_jjc','card_total_play_out_jjc','card_rarity','card_cost','updatetime','card_total_play_out','card_popularity_Deck_jjc']
#卡牌详情
class CardSerializer(serializers.ModelSerializer):##获取卡牌详情
    """
    公告序列化
    """
    updatetime = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = ALL_cards
        fields = "__all__"



class Card_pctSerializer(serializers.ModelSerializer):##获取详情
    """
    公告序列化
    """
    Group_as_of_info = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Card_pct
        fields = "__all__"

#原型列表
class AllCardGroupSerializer(serializers.ModelSerializer):##原型列表
    """
    公告序列化
    """
    Group_as_of = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')


    Group_picture = serializers.SerializerMethodField()
    # pct = serializers.SerializerMethodField()


    def get_Group_picture(self, obj):

        url = 'https://119.23.72.247/media/player_icon/{}.png'.format(obj.Group_player_class_name)

        return url

    # def get_pct(self,obj):
    #     try:
    #         re = Card_pct.objects.filter(Group_id=obj.Group_id)[0] # 获取查询集
    #         dict ={
    #             'Group_win_rate':re.Group_win_rate,
    #             'Group_total_games': re.Group_total_games,
    #             'Group_pct_of_total': re.Group_pct_of_total,
    #             'Group_pct_of_class': re.Group_pct_of_class,
    #
    #         }
    #         return dict
    #     except Exception as e:
    #
    #         return None


    class Meta:
        model = Card_group
        fields = ['Group_id','Group_as_of','Group_name','Group_id','Group_player_class','Group_player_class_name','Group_components','Group_picture','Group_total_games','Group_win_rate']


#原型详情
class CardGroupSerializer(serializers.ModelSerializer):
    """
    公告序列化
    """
    Group_as_of = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    most_deck = serializers.SerializerMethodField()
    back_png =serializers.SerializerMethodField()
    # # pct = serializers.SerializerMethodField()

    Group_picture = serializers.SerializerMethodField()

    # pct = serializers.SerializerMethodField()

    def get_Group_picture(self, obj):
        url = 'https://119.23.72.247/media/player_icon/{}.png'.format(obj.Group_player_class_name)
        return url
    def get_back_png(self, obj):

        url ='https://119.23.72.247/media/player_image/{}.jpg'.format(obj.Group_player_class_name)

        return url


    def get_most_deck(self, obj):



        most_win = Deck_info.objects.filter(Deck_archetype_id=obj.Group_id).order_by('-Deck_win_rate')[0]
        most_total = Deck_info.objects.filter(Deck_archetype_id=obj.Group_id).order_by('-Deck_total_games')[0]

        dict={
            'most_win':most_win.Deck_deck_id,
            'most_win_num':most_win.Deck_total_games,
            'most_win_win':most_win.Deck_win_rate,

            'most_total':most_total.Deck_deck_id,
            'most_total_num': most_total.Deck_total_games,
            'most_total_win':most_total.Deck_win_rate,

        }


        return dict

    class Meta:
        model = Card_group
        fields = ['Group_id','Group_name','Group_player_class','Group_player_class_name','Group_as_of','Group_components','Group_URL','Group_pct_of_class','Group_pct_of_total','Group_total_games','Group_win_rate','Group_as_of_info','most_deck','back_png','Group_picture']
        # fields =   "__all__"
#原型对抗
class Card_duikangSerializer(serializers.ModelSerializer):##获取详情
    """
    公告序列化
    """
    upda_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    hit_group_name = serializers.SerializerMethodField()
    def get_hit_group_name(self, obj):
            try:
                res = Card_group.objects.get(Group_id=obj.hit_Group_id)
                if res:
                    dict ={
                        'hit_group_name':res.Group_name,
                        'hit_group_image':res.Group_image,
                        'hit_group_career':res.Group_player_class_name
                    }


                    return dict
            except:
                dict ={
                    'hit_group_name':None,
                    'hit_group_image':None,
                    'hit_group_career': None,
                }
                return dict

    class Meta:
        model = Card_duikang
        # fields = "__all__"
        fields =['Group_id','hit_Group_id','total_games','win_rate','upda_time','hit_group_name']


##卡组列表
class Deck_infoSerializer(serializers.ModelSerializer):
    """
    公告序列化
    """
    # Group_as_of_info = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    group_player_info = serializers.SerializerMethodField()

    def get_group_player_info(self, obj):


        group_player_info =Card_group.objects.get(Group_id=obj.Deck_archetype_id)
        dict = {
            'Group_name':group_player_info.Group_name,
            'Group_player_class_name':group_player_info.Group_player_class_name,
            'Deck_image':'https://119.23.72.247/media/player_icon/{}.jpg'.format(group_player_info.Group_player_class_name)
        }
        return dict

    class Meta:
        model = Deck_info
        # fields = "__all__"
        fields =['Deck_deck_id','Deck_total_games','Deck_win_rate','cost_total','group_player_info']

#卡组详情

class Deck_info_DetailSerializer(serializers.ModelSerializer):
    """
    公告序列化
    """
    # Group_as_of_info = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    group_player_info = serializers.SerializerMethodField()
    cards_list = serializers.SerializerMethodField()

    def get_cards_list(self, obj):


        card_list = str(obj.Deck_deck_list)[2:-2].split('],[')
        dict_list = []
        card_info ={}
        for card in card_list:
            card_info[card.split(',')[0]]=card.split(',')[1]



        car_list_search = [i for i,value in card_info.items()]
        card_list = ALL_cards.objects.filter(card_dbf_id__in=car_list_search).order_by('card_cost')
        dict_list_reture=[]
        for card in card_list:

            dict = {
                'card_id':card.card_id,
                'card_dbf_id':card.card_dbf_id,
                'card_name':card.card_name,
                'card_type':card.card_type,
                'card_rarity':card.card_rarity,
                'card_cost':card.card_cost,
                'card_image':card.card_image,
                'number':card_info[card.card_dbf_id]

            }
            dict_list_reture.append(dict)
        return dict_list_reture

    def get_group_player_info(self, obj):


        group_player_info =Card_group.objects.get(Group_id=obj.Deck_archetype_id)
        dict = {
            'Group_name':group_player_info.Group_name,
            'Group_player_class_name':group_player_info.Group_player_class_name
        }
        return dict

    class Meta:
        model = Deck_info
        # fields = "__all__"
        fields =['Deck_deck_id','Deck_avg_game_length_seconds','Deck_avg_num_player_turns','Deck_total_games','Deck_win_rate','cost_total','group_player_info','cards_list']


#卡组对抗
class Deck_hit_infoSerializer(serializers.ModelSerializer):
    """
    公告序列化
    """
    Deck_UP_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')


    class Meta:
        model = Deck_hit_info
        fields = "__all__"

class Player_classSerializer(serializers.ModelSerializer):##获取详情
    """
    公告序列化
    """
    Deck_UP_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Player_class
        fields = "__all__"

