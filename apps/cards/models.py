from django.db import models
from datetime import datetime
# Create your models here.
class ALL_cards(models.Model):

    card_dbf_id = models.CharField(default='',max_length=200,verbose_name='hsreplay_dbf_ID')
    card_id = models.CharField(default='',max_length=200,verbose_name='hsreplay_ID',blank=True)
    card_name = models.CharField(default='',max_length=200,verbose_name='卡牌中文名',blank=True)
    card_en_name = models.CharField(default='',max_length=200,verbose_name='卡牌英文名',blank=True)
    card_text = models.CharField(default='', max_length=200, verbose_name='卡牌文字',blank=True)
    card_type = models.CharField(default='', max_length=200, verbose_name='卡牌类型',help_text='（随从(MINION)，法术(SPELL)，武器(WEAPON)，英雄(HERO)）',blank=True)
    card_rarity = models.CharField(default='', max_length=200, verbose_name='卡牌稀有度',help_text='（基础卡(FREE)，普通(COMMON)，稀有(RARE)，史诗(EPIC)，传说(LEGENDARY)）',blank=True)
    card_cardClass = models.CharField(default='', max_length=200, verbose_name='卡牌职业',help_text='战士(WARRIOR)，法师(MAGE)，盗贼(ROGUE)，猎人(HUNTER)，德鲁伊(DRUID)，萨满(SHAMAN)，圣骑士(PALADIN)，牧师(PRIEST)，术士(WARLOCK)',blank=True)
    card_cost = models.CharField(default='', max_length=200, verbose_name='卡牌费用',blank=True)
    is_standard = models.BooleanField(default=False,verbose_name='是否是标准环境卡牌',max_length=200,blank=True)
    card_set = models.CharField(default='',verbose_name='属于扩展包',help_text='基础卡（CORE）,经典（EXPERT1），（奥丹姆）ULDUM，暗影崛起（DALARAN），拉斯塔哈的大乱斗（TROLL），砰砰计划（BOOMSDAY），女巫森林（GILNEAS），狗头人与地下世界（LOOTAPALOOZA），冰封的王座（ICECROWN），勇闯安戈洛（UNGORO），龙争虎斗加基森（GANGS），卡拉赞之夜（KARA），上古之神的低语（OG），探险者协会（LOE），冠军的试炼（TGT），黑石山的火焰（BRM），地精大战侏儒（GVG），纳克萨玛斯（NAXX），荣誉室（HOF）',max_length=200,blank=True)
    card_race = models.CharField(default='',verbose_name='种族',help_text='',max_length=200,blank=True)
    card_mechanism = models.CharField(default='',verbose_name='机制',help_text='战吼',max_length=200,blank=True)
    card_image = models.CharField(default='',verbose_name='图片',help_text='图片',max_length=500,blank=True)
    card_min_image = models.CharField(default='',verbose_name='缩略图',help_text='缩略图',max_length=500,blank=True)

    card_popularity_play_out =models.FloatField(default=0,verbose_name=u'打出卡牌中占比',help_text=u'在所有牌中这张卡牌被打出的概率',blank=True,)
    card_winrate_play_out =models.FloatField(default=0,verbose_name=u'打出胜率',help_text=u'在任何时刻打出的卡牌的平均胜率',blank=True,)
    card_total_play_out =models.FloatField(default=0,verbose_name=u'打出次数',help_text=u'这张卡牌打出的次数',blank=True,)
    card_popularity_Deck =models.FloatField(default=0,verbose_name=u'卡组出现概率',help_text=u'套牌中至少包含一张该卡的概率',blank=True,)
    card_winrate_Deck =models.FloatField(default=0,verbose_name=u'卡组胜率',help_text=u'携带这张卡组的平均概率',blank=True,)
    card_count_Deck =models.FloatField(default=0,verbose_name=u'卡组张数',help_text=u'套牌中平均携带数量',blank=True)
    card_Deck_Deck =models.FloatField(default=0,verbose_name=u'卡组数',help_text=u'套牌总数',blank=True)

    card_popularity_play_out_jjc =models.FloatField(default=0,verbose_name=u'jjc打出卡牌中占比',help_text=u'在所有牌中这张卡牌被打出的概率',blank=True,)
    card_winrate_play_out_jjc =models.FloatField(default=0,verbose_name=u'jjc打出胜率',help_text=u'在任何时刻打出的卡牌的平均胜率',blank=True,)
    card_total_play_out_jjc =models.FloatField(default=0,verbose_name=u'jjc打出次数',help_text=u'这张卡牌打出的次数',blank=True,)
    card_popularity_Deck_jjc =models.FloatField(default=0,verbose_name=u'jjc卡组出现概率',help_text=u'套牌中至少包含一张该卡的概率',blank=True,)
    card_winrate_Deck_jjc =models.FloatField(default=0,verbose_name=u'jjc卡组胜率',help_text=u'携带这张卡组的平均概率',blank=True,)
    card_count_Deck_jjc =models.FloatField(default=0,verbose_name=u'jjc卡组张数',help_text=u'套牌中平均携带数量',blank=True)
    card_Deck_Deck_jjc =models.FloatField(default=0,verbose_name=u'jjc卡组数',help_text=u'套牌总数',blank=True)

    card_popularity_play_out_kuangye =models.FloatField(default=0,verbose_name=u'狂野打出卡牌中占比',help_text=u'狂野在所有牌中这张卡牌被打出的概率',blank=True,)
    card_winrate_play_out_kuangye =models.FloatField(default=0,verbose_name=u'狂野打出胜率',help_text=u'狂野在任何时刻打出的卡牌的平均胜率',blank=True,)
    card_total_play_out_kuangye =models.FloatField(default=0,verbose_name=u'狂野打出次数',help_text=u'狂野这张卡牌打出的次数',blank=True,)
    card_popularity_Deck_kuangye =models.FloatField(default=0,verbose_name=u'狂野卡组出现概率',help_text=u'狂野套牌中至少包含一张该卡的概率',blank=True,)
    card_winrate_Deck_kuangye =models.FloatField(default=0,verbose_name=u'狂野卡组胜率',help_text=u'狂野携带这张卡组的平均概率',blank=True,)
    card_count_Deck_kuangye =models.FloatField(default=0,verbose_name=u'狂野卡组张数',help_text=u'狂野套牌中平均携带数量',blank=True)
    card_Deck_Deck_kuangye =models.FloatField(default=0,verbose_name=u'狂野卡组数',help_text=u'狂野套牌总数',blank=True)
    jjc_update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间",help_text='更新时间')
    updatetime = models.DateTimeField(default=datetime.now, verbose_name="更新时间",help_text='更新时间')



    class Meta:
        verbose_name = "所有狂野加标准卡牌卡牌,，来自hsreplay"
        verbose_name_plural = verbose_name

class Card_group(models.Model):
    Group_name = models.CharField(default='', max_length=200, verbose_name='原型名称')
    Group_id = models.IntegerField(default=0, verbose_name='原型ID', blank=True,primary_key=True)
    Group_image =models.CharField(default='',verbose_name='原型图片',max_length=500)
    Group_player_class = models.IntegerField(default=0, verbose_name=u'类别ID', help_text=u'什么职业的卡组id',
                                              blank=True)
    Group_player_class_name = models.CharField(default=0, max_length=200, verbose_name=u'类别', help_text=u'什么职业的卡组',
                                             blank=True)
    # Group_as_of = models.CharField(default=0, max_length=200, verbose_name=u'更新时间', help_text=u'原型加入时间',
    #                                          blank=True)

    Group_as_of = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name=u'更新时间',help_text=u'原型加入时间',
                                            default=datetime.now)

    Group_components = models.CharField(default=0, max_length=200, verbose_name=u'原型关键组成', help_text=u'卡组关键组成',
                                      blank=True)
    Group_URL = models.CharField(default=0, max_length=200, verbose_name=u'原型URL', help_text=u'卡组URL',
                                           blank=True)
    # Group_recent3_average_hot = models.FloatField(default=0,verbose_name=u'原型近三天的平均热度',help_text=u'原型近三天的平均热度',blank=True,)
    # Group_recent3_average_win = models.FloatField(default=0,verbose_name=u'原型近三天的平均胜率',help_text=u'原型近三天的平均胜率',blank=True,)

    Group_pct_of_class = models.FloatField(default=0, verbose_name=u'近七天原型占该职业的套牌的百分比', help_text=u'近七天原型占该职业的套牌的百分比',
                                           blank=True, )
    Group_pct_of_total = models.FloatField(default=0, verbose_name=u'近七天原型占所有的套牌的百分比', help_text=u'近七天原型占所有的套牌的百分比',
                                           blank=True, )
    Group_total_games = models.FloatField(default=0, verbose_name=u'近七天原型总对局', help_text=u'近七天原型总对局', blank=True, )
    Group_win_rate = models.FloatField(default=0, verbose_name=u'近七天原型总对局胜率', help_text=u'近七天原型总对局胜率', blank=True, )

    Group_as_of_info = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name=u'原型对局信息更新时间',help_text=u'原型对局信息更新时间',
                                            default=datetime.now)
    # Group_as_of_info = models.CharField(default=0, max_length=200, verbose_name=u'原型对局信息更新时间', help_text=u'原型对局信息更新时间',
    #                                          blank=True)

    class Meta:
        verbose_name = "卡组原型，信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.Group_name

    def get_win(self):
        try:
            order =self.card_pct_set.get(Group_id=self.Group_id).Group_win_rate
            return order
        except :
            return 0



class Card_duikang(models.Model):
    Group_id = models.ForeignKey(Card_group, on_delete=models.CASCADE,verbose_name='原型id', help_text=u'原型id')
    hit_Group_id = models.IntegerField(default=0,  verbose_name='原型对抗id' ,help_text=u'原型对抗id')
    total_games =models.FloatField(default=0,verbose_name=u'近七天原型对抗总对局',help_text=u'近七天原型对抗总对局',blank=True,)
    win_rate =models.FloatField(default=0,verbose_name=u'近七天原对抗胜率',help_text=u'近七天原对抗胜率',blank=True,)
    # upda_time =  models.CharField(default=0, max_length=200, verbose_name=u'原型对局信息更新时间', help_text=u'原型对局信息更新时间',
    #                                          blank=True)
    upda_time = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name=u'原型对局信息更新时间',help_text=u'原型对局信息更新时间',
                                            default=datetime.now)

    class Meta:
        verbose_name = "卡组原型，对抗胜率"
        verbose_name_plural = verbose_name

class Card_pct(models.Model):

    # Group_id = models.IntegerField(default=0, verbose_name='原型ID', blank=True)
    Group_id = models.ForeignKey(Card_group, verbose_name='原型ID')


    Group_pct_of_class = models.FloatField(default=0, verbose_name=u'近七天原型占该职业的套牌的百分比', help_text=u'近七天原型占该职业的套牌的百分比',
                                           blank=True, )
    Group_pct_of_total = models.FloatField(default=0, verbose_name=u'近七天原型占所有的套牌的百分比', help_text=u'近七天原型占所有的套牌的百分比',
                                           blank=True, )
    Group_total_games = models.FloatField(default=0, verbose_name=u'近七天原型总对局', help_text=u'近七天原型总对局', blank=True, )
    Group_win_rate = models.FloatField(default=0, verbose_name=u'近七天原型总对局胜率', help_text=u'近七天原型总对局胜率', blank=True, )
    # Group_as_of_info = models.CharField(default=0, max_length=200, verbose_name=u'原型对局信息更新时间', help_text=u'原型对局信息更新时间',
    #                                     blank=True)
    Group_as_of_info = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name=u'原型对局信息更新时间',help_text=u'原型对局信息更新时间',
                                            default=datetime.now)

    class Meta:
        verbose_name = "卡组原型，热度，占比"
        verbose_name_plural = verbose_name

class Deck_info(models.Model):
    Deck_archetype_id = models.CharField(default='', max_length=200, verbose_name='卡组原型', help_text=u'卡组原型')

    Deck_avg_game_length_seconds=models.FloatField(default=0,  verbose_name='30天平均对局时长', help_text=u'30天平均对局时长')
    Deck_avg_num_player_turns=models.FloatField(default=0,  verbose_name='30天平均回合数', help_text=u'30天平均回合数')

    Deck_deck_id=models.CharField(default='', max_length=200, verbose_name='卡组id', help_text=u'卡组id')
    Deck_deck_list=models.CharField(default='', max_length=500, verbose_name='卡组', help_text=u'卡组')
    Deck_digest=models.CharField(default='', max_length=200, verbose_name='未知', help_text=u'未知')
    Deck_total_games=models.FloatField(default=0,  verbose_name='近30天总对局样本', help_text=u'近30天对局样本')
    Deck_win_rate=models.FloatField(default=0,  verbose_name='近30天总对局样本胜率', help_text=u'近30天总对局样本胜率')
    Deck_code =models.CharField(default='', max_length=200, verbose_name='卡组代码', help_text=u'卡组代码')
    Group_as_of_info = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name=u'卡组信息更新时间',help_text=u'卡组信息更新时间',
                                            default=datetime.now)
    cost_total = models.IntegerField(default=0,verbose_name='卡组费用',null=True, blank=True,)



    class Meta:
        verbose_name = "套牌信息"
        verbose_name_plural = verbose_name

class Deck_hit_info(models.Model):
    Deck_deck_id = models.CharField(default='', max_length=200, verbose_name='卡组id', help_text=u'卡组id')
    Deck_hit_DRUID = models.FloatField(default=0,  verbose_name='卡组对战德鲁伊胜率', help_text=u'卡组对战德鲁伊胜率')
    Deck_hit_HUNTER = models.FloatField(default=0,  verbose_name='卡组对战猎人胜率', help_text=u'卡组对战猎人胜率')
    Deck_hit_MAGE = models.FloatField(default=0, verbose_name='卡组对战法师胜率', help_text=u'卡组对战法师胜率')
    Deck_hit_WARLOCK = models.FloatField(default=0, verbose_name='卡组对战术士胜率', help_text=u'卡组对战术士胜率')
    Deck_hit_PALADIN = models.FloatField(default=0, verbose_name='卡组对战骑士胜率', help_text=u'卡组对战骑士胜率')
    Deck_hit_PRIEST = models.FloatField(default=0,  verbose_name='卡组对战牧师胜率', help_text=u'卡组对战牧师胜率')
    Deck_hit_ROGUE = models.FloatField(default=0,  verbose_name='卡组对战潜行者胜率', help_text=u'卡组对战潜行者胜率')
    Deck_hit_SHAMAN = models.FloatField(default=0,  verbose_name='卡组对战萨满胜率', help_text=u'卡组对战萨满胜率')
    Deck_hit_WARRIOR = models.FloatField(default=0,  verbose_name='卡组对战战士胜率', help_text=u'卡组对战战士胜率')
    # Deck_UP_time = models.TimeField(default=datetime.now,verbose_name='更新时间' ,help_text=u'更新时间')
    Deck_total_winrate = models.FloatField(default=0,  verbose_name='总体胜率', help_text=u'总体胜率')
    Deck_UP_time = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name=u'卡组对抗更新时间',help_text=u'卡组对抗更新时间',
                                            default=datetime.now)



    class Meta:
        verbose_name = "套牌对抗胜率"
        verbose_name_plural = verbose_name
class Deck_Scheduling_info(models.Model):
    Deck_deck_id = models.CharField(default='', max_length=200, verbose_name='卡组id', help_text=u'卡组id')
    Card_dbf_id = models.FloatField(default=0,  verbose_name='卡牌dbf_id', help_text=u'卡牌dbf_id')
    Card_avg_turn_played_on = models.FloatField(default=0,  verbose_name='卡牌打出平均回合', help_text=u'卡牌打出平均回合')

    Card_avg_turns_in_hand= models.FloatField(default=0,  verbose_name='卡牌留在手中平均回合', help_text=u'卡牌留在手中平均回合')

    Card_keep_percentage = models.FloatField(default=0,  verbose_name='保留率', help_text=u'保留率')
    Card_opening_hand_winrate = models.FloatField(default=0,  verbose_name='起手胜率', help_text=u'起手胜率')
    Card_winrate_when_drawn = models.FloatField(default=0,  verbose_name='抽到胜率', help_text=u'抽到胜率')
    Card_winrate_when_played = models.FloatField(default=0,  verbose_name='打出胜率', help_text=u'打出胜率')


    # Deck_UP_time = models.TimeField(default=datetime.now,verbose_name='更新时间' ,help_text=u'更新时间')
    Deck_UP_time = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name=u'卡组对抗更新时间',help_text=u'卡组对抗更新时间',
                                            default=datetime.now)



    class Meta:
        verbose_name = "卡组卡牌调度"
        verbose_name_plural = verbose_name





class Player_class(models.Model):
    zhiye = models.CharField(default='',verbose_name='职业',help_text=u'职业',max_length=200)
    zhiye_zhongwen = models.CharField(default='',verbose_name='职业中文',help_text=u'职业中文',max_length=200)
    popularity_kuangye =models.FloatField(default=0,  verbose_name='狂野占比', help_text=u'狂野占比')
    total_games_kuangye =models.FloatField(default=0,  verbose_name='狂野总对局', help_text=u'狂野总对局')
    win_rate_kuangye =models.FloatField(default=0,  verbose_name='狂野胜率', help_text=u'狂野胜率')
    popularity_jjc =models.FloatField(default=0,  verbose_name='竞技场占比', help_text=u'竞技场占比')
    total_games_jjc =models.FloatField(default=0,  verbose_name='竞技场总对局', help_text=u'竞技场总对局')
    win_rate_jjc =models.FloatField(default=0,  verbose_name='竞技场胜率', help_text=u'竞技场胜率')
    popularity_biaozhun =models.FloatField(default=0,  verbose_name='标准占比', help_text=u'标准占比')
    total_games_biaozhun =models.FloatField(default=0,  verbose_name='标准总对局', help_text=u'标准总对局')
    win_rate_biaozhun =models.FloatField(default=0,  verbose_name='标准胜率', help_text=u'标准胜率')

    Deck_UP_time = models.DateTimeField(max_length=100, null=True, blank=True, verbose_name=u'职业对抗更新时间',help_text=u'职业对抗更新时间',
                                            default=datetime.now)
    zhiye_image = models.CharField(default='',max_length=500,verbose_name='图片')
    class Meta:
        verbose_name = "各个职业在各个模式下的胜率"
        verbose_name_plural = verbose_name
