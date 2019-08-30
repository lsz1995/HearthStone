# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-09 09:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0018_player_class_zhiye_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_cards',
            name='card_Deck_Deck_jjc',
            field=models.FloatField(blank=True, default=0, help_text='套牌总数', verbose_name='jjc卡组数'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_Deck_Deck_kuangye',
            field=models.FloatField(blank=True, default=0, help_text='狂野套牌总数', verbose_name='狂野卡组数'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_count_Deck_jjc',
            field=models.FloatField(blank=True, default=0, help_text='套牌中平均携带数量', verbose_name='jjc卡组张数'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_count_Deck_kuangye',
            field=models.FloatField(blank=True, default=0, help_text='狂野套牌中平均携带数量', verbose_name='狂野卡组张数'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_popularity_Deck_jjc',
            field=models.FloatField(blank=True, default=0, help_text='套牌中至少包含一张该卡的概率', verbose_name='jjc卡组出现概率'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_popularity_Deck_kuangye',
            field=models.FloatField(blank=True, default=0, help_text='狂野套牌中至少包含一张该卡的概率', verbose_name='狂野卡组出现概率'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_popularity_play_out_jjc',
            field=models.FloatField(blank=True, default=0, help_text='在所有牌中这张卡牌被打出的概率', verbose_name='jjc打出卡牌中占比'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_popularity_play_out_kuangye',
            field=models.FloatField(blank=True, default=0, help_text='狂野在所有牌中这张卡牌被打出的概率', verbose_name='狂野打出卡牌中占比'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_total_play_out_jjc',
            field=models.FloatField(blank=True, default=0, help_text='这张卡牌打出的次数', verbose_name='jjc打出次数'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_total_play_out_kuangye',
            field=models.FloatField(blank=True, default=0, help_text='狂野这张卡牌打出的次数', verbose_name='狂野打出次数'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_winrate_Deck_jjc',
            field=models.FloatField(blank=True, default=0, help_text='携带这张卡组的平均概率', verbose_name='jjc卡组胜率'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_winrate_Deck_kuangye',
            field=models.FloatField(blank=True, default=0, help_text='狂野携带这张卡组的平均概率', verbose_name='狂野卡组胜率'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_winrate_play_out_jjc',
            field=models.FloatField(blank=True, default=0, help_text='在任何时刻打出的卡牌的平均胜率', verbose_name='jjc打出胜率'),
        ),
        migrations.AddField(
            model_name='all_cards',
            name='card_winrate_play_out_kuangye',
            field=models.FloatField(blank=True, default=0, help_text='狂野在任何时刻打出的卡牌的平均胜率', verbose_name='狂野打出胜率'),
        ),
        migrations.AlterField(
            model_name='player_class',
            name='Deck_UP_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='职业对抗更新时间', max_length=100, null=True, verbose_name='职业对抗更新时间'),
        ),
    ]