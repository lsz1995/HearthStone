import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1", "root", "123456", "lushi", charset='utf8' )
heards = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3',
    'referer': 'https://hsreplay.net/'
}
import requests
import json
def get_all_cars_dbfid():
    url ='https://hsreplay.net/analytics/query/card_played_popularity_report/?GameType=RANKED_WILD&TimeRange=CURRENT_PATCH&RankRange=ALL'
    res = requests.get(url,headers = heards).text
    # print(res)
    data = json.loads(res)['series']['data']['ALL']

    # url2 = 'https://hsreplay.net/analytics/query/card_included_popularity_report/?GameType=RANKED_STANDARD&TimeRange=CURRENT_PATCH&RankRange=ALL'
    # res = requests.get(url2, headers=heards).text
    # data2 = json.loads(res)['series']['data']['ALL']
    return data




def get_cards_info():


#############卡牌信息#########
    url = 'https://hsreplay.net/analytics/query/card_played_popularity_report/?GameType=RANKED_STANDARD&TimeRange=CURRENT_PATCH&RankRange=ALL'
    card_played_popularity_report = requests.get(url,headers =heards).text
    date = json.loads(card_played_popularity_report)['as_of']
    card_played_popularity_report_data = json.loads(card_played_popularity_report)['series']['data']['ALL']
    for i in card_played_popularity_report_data:

        if i['dbf_id']==42630:
            print(i)

###########卡组信息###################
    url1 = 'https://hsreplay.net/analytics/query/card_included_popularity_report/?GameType=RANKED_STANDARD&TimeRange=CURRENT_PATCH&RankRange=ALL'
    card_included_popularity_report= requests.get(url1,headers=heards).text
    card_included_popularity_report_data = json.loads(card_included_popularity_report)['series']['data']['ALL']


    for i in card_included_popularity_report_data:

        if i['dbf_id'] == 42630:
            print(i)


def get_info():
    with open("F:\HearthStone\data\cards.json", 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    for i in load_dict:

        try:
            id = i['dbfId']
        except:
            print('没有ID')

        user_email = ALL_cards.objects.filter(card_dbf_id=id)
        # print(len(user_email))
        if len(user_email) != 0:

            user_email[0].card_id = i['id']

            user_email[0].card_name = i['name']
            user_email[0].card_en_name = i['artist']
            user_email[0].card_text = i.get('text', '')
            user_email[0].card_type = i['type']
            user_email[0].card_rarity = i['rarity']
            user_email[0].card_cardClass = i['cardClass']
            user_email[0].card_cost = i['cost']
            if i['set'] in ['CORE', 'EXPERT1', 'DALARAN', 'TROLL', 'BOOMSDAY', 'GILNEAS']:
                user_email[0].is_standard = True

            user_email[0].card_set = i['set']
            user_email[0].card_race = i.get('race', '')
            user_email[0].card_mechanism = i.get('mechanics', '')
            user_email[0].card_image = 'https://art.hearthstonejson.com/v1/tiles/{}.png'.format(i['id'])
            user_email[0].card_min_image = 'https://art.hearthstonejson.com/v1/render/latest/zhCN/512x/{}.png'.format(
                i['id'])
            user_email[0].save()
            print(user_email[0].card_name)
            print('保存')

if __name__ == '__main__':
    data = get_all_cars_dbfid()  #获取所有有统计的卡牌dbf_id
    get_info()#从最新的data.json 将卡牌基本信息录入

    print(len(data))