import MySQLdb

import json
from datetime import datetime
from .models import ALL_cards,Card_group,Card_duikang,Card_pct,Deck_info,Deck_hit_info,Deck_Scheduling_info
import requests
import re
from random import choice
import time
import random
from unit.IPfuntion import get_proxy,getHtml

class LUSHI_UPDATA:
    def __init__(self):
        print('连接数据库')
        # self.coon = cx_Oracle.connect('SCOTT', '123456', '10.19.2.101:1521/orcl')
        # self.db = MySQLdb.connect("127.0.0.1", "root", "123456", "lushi", charset='utf8' )
        # self.cursor = self.db.cursor()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3',
            'referer': 'https://hsreplay.net/'
        }

        self.USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",

        ]
        self.cookies = {
            # 'cookie':'__cfduid=d708c437d41baf2c6c0d350702c3f8b561564109846; sessionid=rus7qkp78rvxfrswwako9aoi0hif18xk; _ga=GA1.2.856284928.1564109847; __gads=ID=eb5dfe25cfe42274:T=1564109856:S=ALNI_MZaPF5O4hkIriXbbHVN_Hmbo4RzGg; arcane-tracker-download-popup-closed=1; _gid=GA1.2.1765829094.1564366211; twitch-vods-popup-decks-closed=1; csrftoken=VUxcPHKUmm66mR9cYM0P5Wj5d4aN4qNXbms1LAgtuCRUJlrY72thE3bu95AV3asL; _gat=1; django_language=zh-hans',
            'django_language': 'zh-hans'
        }
    def CreatUserAgents(self):
        headers = {
            'user-agent': '{}'.format(choice(self.USER_AGENTS)),
            'referer': 'https://hsreplay.net/'
        }
        return headers
    
    def UP_DATA_CARDS(self):
        '''
        将所有狂野卡牌dbf_id  记录在数据

        :return:
        '''


        #包含狂野的卡牌信息
        url = 'https://hsreplay.net/analytics/query/card_played_popularity_report/?GameType=RANKED_WILD&TimeRange=CURRENT_PATCH&RankRange=ALL'
        card_played_popularity_report = requests.get(url, headers = self.CreatUserAgents()).text
        date = datetime.now()
        card_played_popularity_report_data = json.loads(card_played_popularity_report)['series']['data']['ALL']
        for i in card_played_popularity_report_data:
            each_data = ALL_cards.objects.filter(card_dbf_id=i['dbf_id'])
            if len(each_data) == 1:
                print(i['dbf_id'])

            elif len(each_data)==0:
                print(i['dbf_id'])
                obj_video = ALL_cards.objects.create(
                    card_dbf_id = i['dbf_id']
                )


        # print(res)


    def UP_DATA_EVERY_DAY(self):
        '''
        更新每天的卡牌胜率
        :return:
        '''

        #############卡牌信息#########
        #标准卡牌打出报告


        url_biaozhun_play = 'https://hsreplay.net/analytics/query/card_played_popularity_report/?GameType=RANKED_STANDARD&TimeRange=CURRENT_PATCH&RankRange=ALL'
        # 标准  RANKED_STANDARD   CURRENT_PATCH:当前补丁  标准卡牌占比报告
        url_biaozhun_include = 'https://hsreplay.net/analytics/query/card_included_popularity_report/?GameType=RANKED_STANDARD&TimeRange=CURRENT_PATCH&RankRange=ALL'


        card_played_popularity_report = requests.get(url_biaozhun_play, headers = self.CreatUserAgents()).text
        card_played_popularity_report_data = json.loads(card_played_popularity_report)['series']['data']['ALL']
        date = json.loads(card_played_popularity_report)['as_of']
        print('卡牌胜率：',len(card_played_popularity_report_data))
        for i in card_played_popularity_report_data:
            try:
                each_data = ALL_cards.objects.filter(card_dbf_id=i['dbf_id'])[0]
                each_data.card_popularity_play_out = float(i['popularity'])
                each_data.card_winrate_play_out = float(i['winrate'])
                each_data.card_total_play_out = float(i['total'])
                each_data.updatetime = date
                each_data.save()
            except Exception as e:
                pass
                # print('标准')
                # print(i['dbf_id'])
                # print('没有这张卡的胜率')

        ###########卡组信息###################
        card_included_popularity_report = requests.get(url_biaozhun_include, headers = self.CreatUserAgents()).text
        card_included_popularity_report_data = json.loads(card_included_popularity_report)['series']['data']['ALL']
        print('卡牌胜率：', len(card_included_popularity_report_data))
        for i in card_included_popularity_report_data:
            try:
                each_data = ALL_cards.objects.filter(card_dbf_id=i['dbf_id'])[0]

                each_data.card_popularity_Deck = float(i['popularity'])

                each_data.card_winrate_Deck = float(i['winrate'])
                each_data.card_count_Deck = float(i['count'])
                each_data.card_Deck_Deck = float(i['decks'])


                each_data.save()
            except Exception as e:
               pass

        # jjc  ARENA

        url_jjc_play = 'https://hsreplay.net/analytics/query/card_played_popularity_report/?GameType=ARENA&TimeRange=CURRENT_EXPANSION'

        url_jjc_include =    'https://hsreplay.net/analytics/query/card_included_popularity_report/?GameType=ARENA&TimeRange=CURRENT_EXPANSION'

        jjc_card_played_popularity_report = requests.get(url_jjc_play, headers=self.CreatUserAgents()).text
        jjc_card_played_popularity_report_data = json.loads(jjc_card_played_popularity_report)['series']['data']['ALL']
        date_jjc = json.loads(jjc_card_played_popularity_report)['as_of']
        print('jjc卡牌胜率：', len(jjc_card_played_popularity_report_data))
        for i in jjc_card_played_popularity_report_data:
            try:
                each_data = ALL_cards.objects.filter(card_dbf_id=i['dbf_id'])[0]
                each_data.card_popularity_play_out_jjc = float(i['popularity'])
                each_data.card_winrate_play_out_jjc = float(i['winrate'])
                each_data.card_total_play_out_jjc = float(i['total'])
                each_data.jjc_update_time = date_jjc
                each_data.save()
            except Exception as e:
                pass

        jjc_card_included_popularity_report = requests.get(url_jjc_include, headers = self.CreatUserAgents()).text
        jjc_card_included_popularity_report_data = json.loads(jjc_card_included_popularity_report)['series']['data']['ALL']
        print('jjc卡牌胜率：', len(jjc_card_included_popularity_report_data))
        for i in jjc_card_included_popularity_report_data:
            try:
                each_data = ALL_cards.objects.filter(card_dbf_id=i['dbf_id'])[0]

                each_data.card_popularity_Deck_jjc = float(i['popularity'])
                each_data.jjc_update_time = date_jjc
                each_data.card_winrate_Deck_jjc = float(i['winrate'])
                each_data.card_count_Deck_jjc = float(i['count'])
                each_data.card_Deck_Deck_jjc = float(i['decks'])
                each_data.save()
            except Exception as e:
                pass


        url_kuangye_play='https://hsreplay.net/analytics/query/card_played_popularity_report/?GameType=RANKED_WILD&TimeRange=CURRENT_EXPANSION&RankRange=ALL'
        url_kuangye_include  = 'https://hsreplay.net/analytics/query/card_included_popularity_report/?GameType=RANKED_WILD&TimeRange=CURRENT_EXPANSION&RankRange=ALL'


        ky_card_played_popularity_report = requests.get(url_kuangye_play, headers=self.CreatUserAgents()).text
        ky_card_played_popularity_report_data = json.loads(ky_card_played_popularity_report)['series']['data']['ALL']
        # date = json.loads(ky_card_played_popularity_report)['as_of']
        print('ky卡牌胜率：', len(ky_card_played_popularity_report_data))
        for i in ky_card_played_popularity_report_data:
            try:
                each_data = ALL_cards.objects.filter(card_dbf_id=i['dbf_id'])[0]
                each_data.card_popularity_play_out_kuangye = float(i['popularity'])
                each_data.card_winrate_play_out_kuangye = float(i['winrate'])
                each_data.card_total_play_out_kuangye = float(i['total'])
                # each_data.updatetime = date
                each_data.save()
            except Exception as e:
                pass







        # 狂野  RANKED_WILD

        ky_card_included_popularity_report = requests.get(url_kuangye_include, headers = self.CreatUserAgents()).text
        ky_card_included_popularity_report_data = json.loads(ky_card_included_popularity_report)['series']['data']['ALL']
        print('ky卡牌胜率：', len(ky_card_included_popularity_report_data))
        for i in ky_card_included_popularity_report_data:
            try:
                each_data = ALL_cards.objects.filter(card_dbf_id=i['dbf_id'])[0]

                each_data.card_popularity_Deck_kuangye = float(i['popularity'])

                each_data.card_winrate_Deck_kuangye = float(i['winrate'])
                each_data.card_count_Deck_kuangye = float(i['count'])
                each_data.card_Deck_Deck_kuangye = float(i['decks'])
                each_data.save()
            except Exception as e:
                pass

        print('每天的卡牌胜率更新完成')



    def UP_CARDS_INFO(self):
        '''
        更新卡牌基本信息， 用card.json
        :return:
        '''
        all_json_url ='https://api.hearthstonejson.com/v1/latest/zhCN/cards.json'
        res = requests.get(all_json_url, headers = self.CreatUserAgents()).text
        load_dict = json.loads(res)

        for i in load_dict:
                try:
                    id = i['dbfId']
                except:
                    print('没有ID')

                user_email = ALL_cards.objects.filter(card_dbf_id=id)
                # print(len(user_email))
                if len(user_email)!=0:

                    user_email[0].card_id = i['id']

                    user_email[0].card_name =i['name']
                    user_email[0].card_en_name =i['artist']
                    user_email[0].card_text =i.get('text','')
                    user_email[0].card_type =i['type']
                    user_email[0].card_rarity =i['rarity']
                    user_email[0].card_cardClass =i['cardClass']
                    user_email[0].card_cost =i['cost']
                    if i['set'] in ['CORE','EXPERT1','DALARAN','TROLL','BOOMSDAY','GILNEAS','ULDUM','ULDUM']:
                        user_email[0].is_standard =True


                    user_email[0].card_set =i['set']
                    user_email[0].card_race =i.get('race','')
                    user_email[0].card_mechanism =i.get('mechanics','')
                    user_email[0].card_image ='https://art.hearthstonejson.com/v1/tiles/{}.png'.format(i['id'])
                    user_email[0].card_min_image ='https://art.hearthstonejson.com/v1/render/latest/zhCN/512x/{}.png'.format(i['id'])
                    user_email[0].save()
                    # print(user_email[0].card_name)
                    # print('保存')

        print('每天的卡牌基本信息更新完成')

    def UPDATA_GROUP_all(self):#卡组原型记录更新



        '''
        #卡组原型每天的胜率  近一个月的卡组热度和胜率  20-传说  舍弃
        https://hsreplay.net/analytics/query/single_archetype_stats_over_time/?GameType=RANKED_STANDARD&RankRange=LEGEND_THROUGH_TWENTY&archetype_id=301

        #卡组原型基本信息 archetype_id  id   pct_of_class占法师套牌百分比  pct_of_total占所有套牌百分比 total_games 所有游戏 win_rate 在所有游戏的胜率  近七天
        https://hsreplay.net/analytics/query/archetype_popularity_distribution_stats/?GameType=RANKED_STANDARD&RankRange=LEGEND_THROUGH_TWENTY&TimeRange=LAST_7_DAYS

        #套牌 信息
        https://hsreplay.net/analytics/query/list_decks_by_win_rate/?GameType=RANKED_STANDARD&RankRange=LEGEND_THROUGH_TWENTY&TimeRange=LAST_30_DAYS


        #卡组原型对抗胜率
        https://hsreplay.net/analytics/query/head_to_head_archetype_matchups/?GameType=RANKED_STANDARD&RankRange=LEGEND_THROUGH_TWENTY&TimeRange=LAST_7_DAYS
        :return:
        '''
        url ='https://hsreplay.net/api/v1/archetypes/'
        res = requests.get(url, headers = self.CreatUserAgents(),cookies=self.cookies).text#
        res = json.loads(res)
        for i in res:

            each_data = Card_group.objects.filter(Group_id=i['id'])
            if len(each_data) == 1:
                # print('存在')
                # print('更新前：',each_data[0].Group_as_of)

                if i['standard_ccp_signature_core'] != None:
                    Card_group.objects.filter(Group_id=i['id']).update(
                        Group_id = i['id'],
                        Group_name =i['name'],
                        Group_player_class =i['player_class'],
                        Group_player_class_name =i['player_class_name'],
                        Group_as_of =i['standard_ccp_signature_core']['as_of'],
                        Group_components =i['standard_ccp_signature_core']['components'],
                        Group_URL =i['url'],
                        Group_image = 'https://119.23.72.247/media/player_icon/{}.png'.format(i['player_class_name'])
                    )
                elif i['standard_ccp_signature_core'] == None:
                    Card_group.objects.filter(Group_id=i['id']).update(
                        Group_id=i['id'],
                        Group_name=i['name'],
                        Group_player_class=i['player_class'],
                        Group_player_class_name=i['player_class_name'],
                        # Group_as_of=i['standard_ccp_signature_core']['as_of'],
                        # Group_components=i['standard_ccp_signature_core']['components'],
                        Group_URL=i['url'],
                        Group_image='https://119.23.72.247/media/player_icon/{}.png'.format(i['player_class_name'])

                    )
                # print('更新后：',Card_group.objects.filter(Group_id=i['id'])[0].Group_as_of)
            elif len(each_data) == 0:
                print('原型不存在，新增')
                if i['standard_ccp_signature_core'] != None:
                    obj_video = Card_group.objects.create(
                        Group_id = i['id'],
                        Group_name =i['name'],
                        Group_player_class =i['player_class'],
                        Group_player_class_name =i['player_class_name'],

                        Group_as_of =i['standard_ccp_signature_core']['as_of'],
                        Group_components =i['standard_ccp_signature_core']['components'],
                        Group_image='https://119.23.72.247/media/player_icon/{}.png'.format(i['player_class_name']),
                        Group_URL =i['url'],
                    )
                elif i['standard_ccp_signature_core'] == None:
                    obj_video = Card_group.objects.create(
                        Group_id=i['id'],
                        Group_name=i['name'],
                        Group_player_class=i['player_class'],
                        Group_player_class_name=i['player_class_name'],
                        # Group_as_of=i['standard_ccp_signature_core']['as_of'],
                        # Group_components=i['standard_ccp_signature_core']['components'],
                        Group_URL=i['url'],
                        Group_image='https://119.23.72.247/media/player_icon/{}.png'.format(i['player_class_name'])

                    )
    # def Get_Group_hot_win_30(self,id):#更新原型hot 和win
    #
    #     win_hot_url = 'https://hsreplay.net/analytics/query/single_archetype_stats_over_time/?GameType=RANKED_STANDARD&RankRange=LEGEND_THROUGH_TWENTY&archetype_id={}'.format(id)
    #     print(win_hot_url)
    #     win_hot_res = requests.get(win_hot_url, headers = self.CreatUserAgents(), cookies=self.cookies).text
    #     if win_hot_res != '':
    #
    #         win_hot = json.loads(win_hot_res)['series']
    #         if len(win_hot[0]['data']) >2:
    #             win = (win_hot[0]['data'][-3]['y']+win_hot[0]['data'][-2]['y']+win_hot[0]['data'][-1]['y'])/3
    #             hot = (win_hot[1]['data'][-3]['y']+win_hot[1]['data'][-2]['y']+win_hot[1]['data'][-1]['y'])/3
    #             Card_group.objects.filter(Group_id=id).update(
    #                 Group_recent3_average_hot = hot,
    #                 Group_recent3_average_win = win,
    #             )
    #         elif len(win_hot[0]['data']) <3 and len(win_hot[0]['data'])!=0:
    #             Card_group.objects.filter(Group_id=id).update(
    #                 Group_recent3_average_hot = win_hot[0]['data'][-1]['y'],
    #                 Group_recent3_average_win = win_hot[1]['data'][-1]['y'],
    #             )
    #
    #
    #
    #
    #     else:
    #         pass

    def GetGroup_pct_info(self):
        '''
        卡组原型胜率热度
        :return:
        '''

        info_url_all ='https://hsreplay.net/analytics/query/archetype_popularity_distribution_stats/?GameType=RANKED_STANDARD&RankRange=LEGEND_THROUGH_TWENTY&TimeRange=LAST_7_DAYS'

        info_res = requests.get(info_url_all, headers = self.CreatUserAgents(), cookies=self.cookies).text

        zhiye_list = json.loads(info_res)['series']['data']
        time = json.loads(info_res)['as_of']


        for i in zhiye_list:

            for j in zhiye_list[i]:
                obj = Card_group.objects.filter(Group_id=j['archetype_id'])
                if len(obj)==0:
                    # print('原型胜率占比不存在')
                    Card_group.objects.create(
                        Group_id=j['archetype_id'],
                        Group_pct_of_class = j['pct_of_class'],
                        Group_pct_of_total = j['pct_of_total'],
                        Group_total_games = j['total_games'],
                        Group_win_rate = j['win_rate'],
                        Group_as_of_info = time,
                    )
                elif len(obj)==1:
                    # print('原型胜率占比存在')
                    Card_group.objects.filter(Group_id=j['archetype_id']).update(
                        Group_id=j['archetype_id'],
                        Group_pct_of_class=j['pct_of_class'],
                        Group_pct_of_total=j['pct_of_total'],
                        Group_total_games=j['total_games'],
                        Group_win_rate=j['win_rate'],
                        Group_as_of_info=time,
                    )

        print('卡组原型胜率热度更新完成')


    def Get_head_to_head_archetype_matchups(self):
        '''
        最近七天的 原型对抗情况
        :return:
        '''

        url = 'https://hsreplay.net/analytics/query/head_to_head_archetype_matchups/?GameType=RANKED_STANDARD&RankRange=LEGEND_THROUGH_TWENTY&TimeRange=LAST_7_DAYS'

        info_res = requests.get(url, headers = self.CreatUserAgents(), cookies=self.cookies).text

        duikang = json.loads(info_res)['series']['data']
        time = json.loads(info_res)['as_of']
        for i in duikang:
            for j in duikang[i]:
                # print(i, '对抗', j)
                obj = Card_duikang.objects.filter(Group_id=i,hit_Group_id=j)
                if len(obj)==1:
                    Card_duikang.objects.filter(Group_id=i,hit_Group_id=j).update(
                        total_games =duikang[i][j]['total_games'],
                        win_rate = duikang[i][j]['win_rate'],
                        upda_time = time
                    )
                elif len(obj)==0:
                    Card_duikang.objects.create(
                        Group_id_id =  i,
                        hit_Group_id =j,
                        total_games =duikang[i][j]['total_games'],
                        win_rate = duikang[i][j]['win_rate'],
                        upda_time = time
                    )
        print('最近七天的 原型对抗情况更新完毕')

    def UP_Decks(self):
        '''
        更新套牌信息
        :return:
        '''
        #全部套牌
    #     https://hsreplay.net/analytics/query/list_decks_by_win_rate/?GameType=RANKED_STANDARD&RankRange=ALL&Region=ALL&PlayerInitiative=ALL
    # 套牌30天的热度与胜率
    # https://hsreplay.net/analytics/query/single_deck_stats_over_time/?GameType=RANKED_STANDARD&RankRange=ALL&Region=ALL&PlayerInitiative=ALL&deck_id=cZC2BsPl8ZAEhvzw6R4d4f
    #套牌对抗职业胜率
    #https://hsreplay.net/analytics/query/single_deck_base_winrate_by_opponent_class/?GameType=RANKED_STANDARD&RankRange=ALL&Region=ALL&PlayerInitiative=ALL&deck_id=cZC2BsPl8ZAEhvzw6R4d4f
    #套牌调度建议
    # https://hsreplay.net/analytics/query/single_deck_mulligan_guide/?GameType=RANKED_STANDARD&RankRange=ALL&Region=ALL&PlayerInitiative=ALL&deck_id=cZC2BsPl8ZAEhvzw6R

        url = 'https://hsreplay.net/analytics/query/list_decks_by_win_rate/?GameType=RANKED_STANDARD&RankRange=ALL&Region=ALL&PlayerInitiative=ALL'
        res = requests.get(url, headers = self.CreatUserAgents(), cookies=self.cookies).text  #
        res = json.loads(res)
        date = res['as_of']
        for i in res['series']['data']:
            for j in res['series']['data'][i]:
                obj = Deck_info.objects.filter(Deck_deck_id=j['deck_id'])
                # print(j['archetype_id'])
                if len(obj)==1:
                    Deck_info.objects.filter(Deck_deck_id=j['deck_id']).update(
                        # Deck_deck_id=j['deck_id'],
                        Deck_deck_list=j['deck_list'],
                        Deck_digest=j['digest'],
                        Deck_win_rate=j['win_rate'],
                        # Deck_code = code,
                        Group_as_of_info=date,
                        Deck_total_games=j['total_games'],
                        Deck_archetype_id=j['archetype_id'],
                        Deck_avg_game_length_seconds=j['avg_game_length_seconds'],
                        Deck_avg_num_player_turns=j['avg_num_player_turns'],
                    )
                elif len(obj) ==0:

                    try:
                        code = self.get_Deck_code(j['deck_id'])
                    except Exception:
                        code='获取失败'
                        print(Exception)
                    card_list = j['deck_list'][2:-2].split('],[')
                    dict_list = []
                    for card in card_list:
                        card = {
                            'id': card.split(',')[0],
                            'number': card.split(',')[1],
                        }
                        dict_list.append(card)
                    car_list = [i['id'] for i in dict_list]
                    card_list = ALL_cards.objects.filter(card_dbf_id__in=car_list)
                    cost_total = 0
                    for each_dict in dict_list:
                        for each_card in card_list:
                            if each_dict['id'] == each_card.card_dbf_id:
                                if each_card.card_rarity == 'FREE':
                                    pass
                                elif each_card.card_rarity == 'COMMON':
                                    cost_total += 40 * int(each_dict['number'])
                                elif each_card.card_rarity == 'RARE':
                                    cost_total += 100 * int(each_dict['number'])
                                elif each_card.card_rarity == 'EPIC':
                                    cost_total += 400 * int(each_dict['number'])
                                elif each_card.card_rarity == 'LEGENDARY':
                                    cost_total += 1600 * int(each_dict['number'])
                    # print(j['archetype_id'])
                    Deck_info.objects.create(
                        Deck_deck_id=j['deck_id'],
                        Deck_deck_list=j['deck_list'],
                        Deck_digest=j['digest'],
                        Deck_win_rate=j['win_rate'],
                        Group_as_of_info=date,
                        Deck_code=code,
                        Deck_total_games=j['total_games'],
                        Deck_archetype_id=j['archetype_id'],
                        Deck_avg_game_length_seconds=j['avg_game_length_seconds'],
                        Deck_avg_num_player_turns=j['avg_num_player_turns'],
                        cost_total=cost_total
                    )
                else:
                    pass
        print('更新套牌信息完成')


    def Get_Deck_hit_info(self):
        all_deck = Deck_info.objects.all()
        print('卡组对抗总共',len(all_deck))
        for i in all_deck:
            try:
                # print(i.Deck_deck_id)
                url ='https://hsreplay.net/analytics/query/single_deck_base_winrate_by_opponent_class/?GameType=RANKED_STANDARD&RankRange=ALL&Region=ALL&PlayerInitiative=ALL&deck_id={}'.format(i.Deck_deck_id)
                # res = requests.get(url, headers = self.CreatUserAgents(), cookies=self.cookies,).text  #
                res =getHtml(url,self.CreatUserAgents(),self.cookies)
                if res:
                    res = json.loads(res)
                    date = res['as_of']
                    obj = Deck_hit_info.objects.filter(Deck_deck_id=i.Deck_deck_id)
                    if len(obj) == 1:
                        Deck_hit_info.objects.filter(Deck_deck_id=i.Deck_deck_id).update(
                            Deck_deck_id=i.Deck_deck_id,
                            Deck_hit_DRUID = res['series']['data']['DRUID'][0]['winrate'],
                            Deck_hit_HUNTER = res['series']['data']['HUNTER'][0]['winrate'],
                            Deck_hit_MAGE = res['series']['data']['MAGE'][0]['winrate'],
                            Deck_hit_WARLOCK = res['series']['data']['WARLOCK'][0]['winrate'],
                            Deck_hit_PALADIN = res['series']['data']['PALADIN'][0]['winrate'],
                            Deck_hit_PRIEST = res['series']['data']['PRIEST'][0]['winrate'],
                            Deck_hit_ROGUE = res['series']['data']['ROGUE'][0]['winrate'],
                            Deck_hit_SHAMAN = res['series']['data']['SHAMAN'][0]['winrate'],
                            Deck_hit_WARRIOR = res['series']['data']['WARRIOR'][0]['winrate'],
                            Deck_total_winrate = res['series']['metadata']['total_winrate'],
                            Deck_UP_time = date,
                        )
                    elif len(obj) == 0:


                        Deck_hit_info.objects.create(
                            Deck_deck_id=i.Deck_deck_id,
                            Deck_hit_DRUID=res['series']['data']['DRUID'][0]['winrate'],
                            Deck_hit_HUNTER=res['series']['data']['HUNTER'][0]['winrate'],
                            Deck_hit_MAGE=res['series']['data']['MAGE'][0]['winrate'],
                            Deck_hit_WARLOCK=res['series']['data']['WARLOCK'][0]['winrate'],
                            Deck_hit_PALADIN=res['series']['data']['PALADIN'][0]['winrate'],
                            Deck_hit_PRIEST=res['series']['data']['PRIEST'][0]['winrate'],
                            Deck_hit_ROGUE=res['series']['data']['ROGUE'][0]['winrate'],
                            Deck_hit_SHAMAN=res['series']['data']['SHAMAN'][0]['winrate'],
                            Deck_hit_WARRIOR=res['series']['data']['WARRIOR'][0]['winrate'],
                            Deck_total_winrate=res['series']['metadata']['total_winrate'],
                            Deck_UP_time=date,

                        )
                    else:
                        pass
                else:
                    pass
            except Exception:
                print(Exception)

        print('卡组对抗更新完毕')



    def Get_Deck_Scheduling_info(self):

            pass
    def Get_Player_class(self):
        from .models import Player_class

        url = 'https://hsreplay.net/analytics/query/player_class_performance_summary/'

        res = requests.get(url, headers = self.CreatUserAgents(), cookies=self.cookies).text  #
        res = json.loads(res)
        date = res['as_of']

        for i in res['series']['data']:
            obj = Player_class.objects.filter(zhiye=i)
            if len(obj) == 0:
                # print('职业不存在')
                Player_class.objects.create(
                    zhiye=i,
                )
            else:
                pass

            # print('更新',i,'信息')
            for j in res['series']['data'][i]:
                # print(type(j['game_type']))
                if j['game_type']==2:#标准
                    add = Player_class.objects.filter(zhiye=i).update(
                        popularity_biaozhun=j['popularity'],
                        total_games_biaozhun=j['total_games'],
                        win_rate_biaozhun=j['win_rate'],
                        Deck_UP_time=date
                    )
                elif j['game_type'] ==3:#狂野
                    add = Player_class.objects.filter(zhiye=i).update(
                        popularity_kuangye=j['popularity'],
                        total_games_kuangye=j['total_games'],
                        win_rate_kuangye=j['win_rate'],
                        Deck_UP_time=date
                    )
                elif  j['game_type'] ==30:#jjc
                    add = Player_class.objects.filter(zhiye=i).update(
                        popularity_jjc=j['popularity'],
                        total_games_jjc=j['total_games'],
                        win_rate_jjc=j['win_rate'],
                        Deck_UP_time=date
                    )
                else:
                    pass



    def get_Deck_code(self,id):#根据卡组ID 获取代码

        url = 'https://hsreplay.net/decks/{}/'.format(id)

        try:
            proxy = get_proxy()

            res = requests.get(url, headers=self.CreatUserAgents(), cookies=self.cookies, timeout=5,proxies={"http": "http://{}".format(proxy)}).text  #
            id  = re.findall(r'content="(.*?)"/>', res)[4]#获取指定视频的 aid值
            return id
        except:
            print('获取卡组代码失败')
            id='获取失败'
            return id





    def __del__(self):
        print('关闭连接')
