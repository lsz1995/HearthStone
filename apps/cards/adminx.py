# -*- coding:utf-8 -*-
import xadmin


from .models import ALL_cards,Card_group,Card_duikang,Card_pct,Deck_info,Deck_Scheduling_info,Deck_hit_info,Player_class

from django.template import loader


class ALL_cardsAdmin(object):
    list_display = ['card_dbf_id','card_id','card_name','card_popularity_play_out','card_winrate_play_out','card_total_play_out','card_popularity_Deck','card_winrate_Deck','card_count_Deck','card_en_name','card_Deck_Deck','card_text','card_type','card_rarity','card_cardClass','card_cost','is_standard','card_set','card_race','card_mechanism','card_image','card_min_image','jjc_update_time']  # 后台管理显示地段
    search_fields = ['card_dbf_id','card_id','card_name','card_popularity_play_out','card_winrate_play_out','card_total_play_out','card_popularity_Deck','card_winrate_Deck','card_count_Deck','card_name','card_en_name','card_Deck_Deck','card_text','card_type','card_rarity','card_cardClass','card_cost','is_standard','card_set','card_race','card_mechanism','card_image','card_min_image','jjc_update_time']   # 后台搜索字段
    list_filter =  ['card_dbf_id','card_id','card_name','card_popularity_play_out','card_winrate_play_out','card_total_play_out','card_popularity_Deck','card_winrate_Deck','card_count_Deck','card_name','card_en_name','card_Deck_Deck','card_text','card_type','card_rarity','card_cardClass','card_cost','is_standard','card_set','card_race','card_mechanism','card_image','card_min_image','jjc_update_time']

class GroupAdmin(object):
    list_display =['Group_id','Group_name','Group_player_class','Group_player_class_name','Group_as_of','Group_components','Group_URL','Group_image']
    search_fields =['Group_id','Group_name','Group_player_class','Group_player_class_name','Group_as_of','Group_components','Group_URL',]
    list_filter =['Group_id','Group_name','Group_player_class','Group_player_class_name','Group_as_of','Group_components','Group_URL',]



class Card_duikangAdmin(object):
    list_display=['Group_id','hit_Group_id','total_games','win_rate','upda_time']
    search_fields=['Group_id','hit_Group_id','total_games','win_rate','upda_time']
    list_filter=['Group_id','hit_Group_id','total_games','win_rate','upda_time']

class Card_pctAdmin(object):
    list_display=['Group_id','Group_pct_of_class','Group_pct_of_total','Group_total_games','Group_win_rate','Group_as_of_info']
    search_fields=['Group_id','Group_pct_of_class','Group_pct_of_total','Group_total_games','Group_win_rate','Group_as_of_info']
    list_filter=['Group_id','Group_pct_of_class','Group_pct_of_total','Group_total_games','Group_win_rate','Group_as_of_info']

class Deck_infoAdmin(object):
    list_display = ['Deck_deck_id', 'Deck_archetype_id', 'Deck_avg_game_length_seconds', 'Deck_avg_num_player_turns', 'Deck_deck_list',
                    'Deck_total_games','Deck_win_rate','Deck_code','Group_as_of_info']
    search_fields = ['Deck_deck_id', 'Deck_archetype_id', 'Deck_avg_game_length_seconds', 'Deck_avg_num_player_turns', 'Deck_deck_list',
                    'Deck_total_games','Deck_win_rate','Deck_code','Group_as_of_info']
    list_filter = ['Deck_deck_id', 'Deck_archetype_id', 'Deck_avg_game_length_seconds', 'Deck_avg_num_player_turns', 'Deck_deck_list',
                    'Deck_total_games','Deck_win_rate','Deck_code','Group_as_of_info']






class Deck_hit_infoAdmin(object):
    list_display = ['Deck_deck_id', 'Deck_hit_DRUID', 'Deck_hit_HUNTER', 'Deck_hit_MAGE', 'Deck_hit_WARLOCK',
                    'Deck_hit_PALADIN','Deck_hit_PRIEST','Deck_hit_ROGUE','Deck_hit_SHAMAN','Deck_hit_WARRIOR','Deck_total_winrate','Deck_UP_time']
    search_fields = ['Deck_deck_id', 'Deck_hit_DRUID', 'Deck_hit_HUNTER', 'Deck_hit_MAGE', 'Deck_hit_WARLOCK',
                    'Deck_hit_PALADIN','Deck_hit_PRIEST','Deck_hit_ROGUE','Deck_hit_SHAMAN','Deck_hit_WARRIOR','Deck_total_winrate','Deck_UP_time']
    list_filter = ['Deck_deck_id', 'Deck_hit_DRUID', 'Deck_hit_HUNTER', 'Deck_hit_MAGE', 'Deck_hit_WARLOCK',
                    'Deck_hit_PALADIN','Deck_hit_PRIEST','Deck_hit_ROGUE','Deck_hit_SHAMAN','Deck_hit_WARRIOR','Deck_total_winrate','Deck_UP_time']


class Player_classAmin(object):
    list_display = ['zhiye', 'popularity_kuangye', 'total_games_kuangye', 'win_rate_kuangye', 'popularity_jjc',
                    'total_games_jjc','win_rate_jjc','popularity_biaozhun','total_games_biaozhun','win_rate_biaozhun','Deck_UP_time']
    search_fields = ['zhiye', 'popularity_kuangye', 'total_games_kuangye', 'win_rate_kuangye', 'popularity_jjc',
                    'total_games_jjc','win_rate_jjc','popularity_biaozhun','total_games_biaozhun','win_rate_biaozhun','Deck_UP_time']
    list_filter = ['zhiye', 'popularity_kuangye', 'total_games_kuangye', 'win_rate_kuangye', 'popularity_jjc',
                    'total_games_jjc','win_rate_jjc','popularity_biaozhun','total_games_biaozhun','win_rate_biaozhun','Deck_UP_time']





xadmin.site.register(ALL_cards,ALL_cardsAdmin)
xadmin.site.register(Deck_hit_info,Deck_hit_infoAdmin)
xadmin.site.register(Deck_info,Deck_infoAdmin)
xadmin.site.register(Card_group,GroupAdmin)
xadmin.site.register(Card_duikang,Card_duikangAdmin)
xadmin.site.register(Card_pct,Card_pctAdmin)
xadmin.site.register(Player_class,Player_classAmin)



