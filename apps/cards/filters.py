import django_filters
from django.db.models import Q
# from .models import ALL_cards
from .models import ALL_cards,Card_group,Card_duikang,Card_pct,Deck_info,Deck_hit_info,Deck_Scheduling_info,Player_class
class AllCard_filters(django_filters.rest_framework.FilterSet):


    # card_list = django_filters.DateFilter(field_name='card_dbf_id', help_text="卡组列表",lookup_expr='gte')#最低时间    print('s')
    # card_dbf_id = django_filters.DateFilter(name='card_dbf_id', help_text="卡组列表",lookup_expr='gte')#最低时间
    # list__card = django_filters.NumberFilter(field_name='card_dbf_id',lookup_expr='icontains')
    card_list = django_filters.CharFilter(method="get_card_list")
    # deck_id = django_filters.CharFilter(method="get_deck_id")
    min_cost = django_filters.CharFilter(method='get_min_cost',)
    min_playout_jjc = django_filters.NumberFilter(name='card_total_play_out_jjc', help_text='jjc最低打出次数', lookup_expr='gte', )
    # min_playout_jjc_time =  django_filters.DateFilter(name='card_dbf_id', help_text="卡组列表",lookup_expr='gte')#最低时间



    def get_min_cost(self,queryset,*arg):


        queryset.filter(card_cost=arg[1])


        if arg[1]!='7':

            try:
                ordering = self.data['ordering']
                return  queryset.filter(card_cost=arg[1]).order_by(ordering)
            except:
                return queryset.filter(card_cost=arg[1])

        if arg[1]=='7':
            try:
                ordering = self.data['ordering']
                return queryset.filter(card_cost=arg[1]).order_by(ordering)
            except:
                return queryset.filter(card_cost=arg[1])
    # def get_deck_id(self, queryset, *arg):
    #
    #     print(arg[1])
    #     print('2wyaL9LJaDaiYXUuHpldv')
    #
    #     return queryset

    def get_card_list(self, queryset, *arg):

        print(arg[1])
        card_list = arg[1][1:-1].replace(' ','').split(',')


        card_list = ALL_cards.objects.filter(card_dbf_id__in=card_list).order_by('card_cost')


        queryset = card_list
        return queryset






    class Meta:
        model = ALL_cards
        fields = ['card_type', 'card_rarity','card_cardClass','card_cost','is_standard','card_set','card_dbf_id','card_list','min_cost','min_playout_jjc',]


class AllCardGroup_filters(django_filters.rest_framework.FilterSet):
    min_Group_total = django_filters.NumberFilter(name='Group_total_games', help_text='最小场数', lookup_expr='gte', )
    min_games_win = django_filters.NumberFilter(name='Group_win_rate', help_text='最小胜率', lookup_expr='gte', )

    class Meta:
        model = Card_group
        # fields = ['Group_name', 'card_rarity','card_cardClass','card_cost','is_standard','card_set']
        fields =['Group_id','Group_name','Group_player_class','Group_player_class_name','Group_as_of','Group_components','Group_URL','min_games_win','min_games_win']


class Card_duikang_filters(django_filters.rest_framework.FilterSet):

    min_hit_Group_id = django_filters.NumberFilter(name='hit_Group_id', help_text='最小id',lookup_expr='gte',)#最大时间
    min_games_total = django_filters.NumberFilter(name='total_games', help_text='最小场数',lookup_expr='gte',)#最大时间

    career  = django_filters.CharFilter(method="get_career", help_text='职业')

    def get_career(self, queryset, *arg):

        import datetime
        obj = Card_group.objects.filter(Group_player_class_name=arg[1]).order_by()
        list = [i.Group_id for i in obj]

        queryset = queryset.filter(hit_Group_id__in=list)

        return queryset

    class Meta:
        model = Card_duikang
        # fields = ['Group_name', 'card_rarity','card_cardClass','card_cost','is_standard','card_set']
        fields =['Group_id','hit_Group_id','total_games','win_rate','upda_time','min_hit_Group_id','min_games_total','career']



class Card_pct_filters(django_filters.rest_framework.FilterSet):




    class Meta:
        model = Card_pct
        # fields = ['Group_name', 'card_rarity','card_cardClass','card_cost','is_standard','card_set']
        fields =['Group_pct_of_class','Group_pct_of_total','Group_total_games','Group_win_rate','Group_as_of_info']

class Deck_info_filters(django_filters.rest_framework.FilterSet):
    career = django_filters.CharFilter(method="get_career", help_text='职业')

    def get_career(self, queryset, *arg):
        import datetime
        obj = Card_group.objects.filter(Group_player_class_name=arg[1]).order_by()
        list = [i.Group_id for i in obj]

        queryset = queryset.filter(Deck_archetype_id__in=list)

        return queryset


    class Meta:
        model = Deck_info
        # fields = ['Group_name', 'card_rarity','card_cardClass','card_cost','is_standard','card_set']
        fields =['Deck_deck_id', 'Deck_archetype_id', 'Deck_avg_game_length_seconds', 'Deck_avg_num_player_turns', 'Deck_deck_list',
                    'Deck_total_games','Deck_win_rate','Deck_code','Group_as_of_info','career']



class Deck_hit_info_filters(django_filters.rest_framework.FilterSet):




    class Meta:
        model = Deck_hit_info
        # fields = ['Group_name', 'card_rarity','card_cardClass','card_cost','is_standard','card_set']
        fields =['Deck_deck_id', 'Deck_hit_DRUID', 'Deck_hit_HUNTER', 'Deck_hit_MAGE', 'Deck_hit_WARLOCK',
                    'Deck_hit_PALADIN','Deck_hit_PRIEST','Deck_hit_ROGUE','Deck_hit_SHAMAN','Deck_hit_WARRIOR','Deck_total_winrate','Deck_UP_time']

class Player_class_filters(django_filters.rest_framework.FilterSet):




    class Meta:
        model = Player_class
        # fields = ['Group_name', 'card_rarity','card_cardClass','card_cost','is_standard','card_set']
        fields =['zhiye', 'popularity_kuangye', 'total_games_kuangye', 'win_rate_kuangye', 'popularity_jjc',
                    'total_games_jjc','win_rate_jjc','popularity_biaozhun','total_games_biaozhun','win_rate_biaozhun','Deck_UP_time']


