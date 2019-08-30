import json


# with open("./cards.json",'r',encoding = 'utf-8') as load_f:
#     load_dict = json.load(load_f)
#
#
#
#
# for i in load_dict:
#     try:
#         print(i)
#         print('**************************')
#         print(i['id'])
#         print(i['dbfId'])
#         print('卡牌名：',i['name'])
#         print('txt：',i['text'])
#         print('类型：',i['type']) #随从还是法术  MINION：随从   SPELL：法术
#         print('稀有度：',i['rarity']) #  COMMON：普通 RARE ：稀有  EPIC：史诗 LEGENDARY：传说
#         print('卡牌职业：',i['cardClass'])  #WARRIOR ：战士  HUNTER：猎人  DRUID：德鲁伊  MAGE：法师 PALADIN：圣骑士 PRIEST：牧师 盗贼：ROGUE 萨满：SHAMAN 术士：WARLOCK 中立：NEUTRAL,一张卡就是随机一套牌：WHIZBANG
#
#     except:
#         print('没有')
#
# import requests
#
# from apps.cards.models import ALL_cards

if __name__ == '__main__':
    # import requests
    #
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3',
    #
    # }
    #
    # url = 'https://hsreplay.net/analytics/query/card_played_popularity_report/?GameType=RANKED_WILD&TimeRange=CURRENT_PATCH&RankRange=ALL'
    # card_played_popularity_report = requests.get(url, headers=headers).text
    # card_played_popularity_report_data = json.loads(card_played_popularity_report)['series']['data']['ALL']
    #
    import random
    import time

    time.sleep(random.uniform(1.1, 5.4))
    print(random.uniform(1.1,5.4))
