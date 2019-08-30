
import requests
import re
import json
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3',

}


url = 'https://pubg.op.gg/user/cunzhang008'

html = requests.get(url,headers=headers).text

cids = re.findall(r'data-user_id="(.*?)"', html)[0]#获取指定视频的 aid值
print(cids)
zhanji_url ='https://pubg.op.gg/api/users/{}/matches/recent?queue_size=1&mode=tpp&type=official'.format(cids)

zhanji = requests.get(zhanji_url,headers=headers).text
zhanjis = json.loads(zhanji)['matches']['items']

for i in zhanjis:
    print(i)
    print('时间：',i['started_at'])
    print('总队伍数',i['total_rank'])
    print('队伍人数',i['queue_size'])
    print('排名',i['participant']['stats']['rank'])
    print('伤害',i['participant']['stats']['combat']['damage']['damage_dealt'])
    print('移动距离',i['participant']['stats']['combat']['distance_traveled']['walk_distance'])
    print('搭载距离',i['participant']['stats']['combat']['distance_traveled']['ride_distance'])
    print('愈合',i['participant']['stats']['combat']['boosts'])
    print('增强',i['participant']['stats']['combat']['heals'])
    print('生存时间',i['participant']['stats']['combat']['time_survived'])
    print('杀人数',i['participant']['stats']['combat']['kda']['kills'])
    print('助攻',i['participant']['stats']['combat']['kda']['assists'])
    print('爆头数',i['participant']['stats']['combat']['kda']['headshot_kills'])
    print('最远击杀',i['participant']['stats']['combat']['kda']['longest_kill'])
    print('击倒',i['participant']['stats']['combat']['kda']['kill_steaks'])
    print('-------------------------------------------------------')



