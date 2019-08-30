# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-03 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0015_deck_hit_info_deck_total_winrate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhiye', models.CharField(default='', help_text='职业', max_length=200, verbose_name='职业')),
                ('popularity_kuangye', models.FloatField(default=0, help_text='狂野占比', verbose_name='狂野占比')),
                ('total_games_kuangye', models.FloatField(default=0, help_text='狂野总对局', verbose_name='狂野总对局')),
                ('win_rate_kuangye', models.FloatField(default=0, help_text='狂野胜率', verbose_name='狂野胜率')),
                ('popularity_jjc', models.FloatField(default=0, help_text='竞技场占比', verbose_name='竞技场占比')),
                ('total_games_jjc', models.FloatField(default=0, help_text='竞技场总对局', verbose_name='竞技场总对局')),
                ('win_rate_jjc', models.FloatField(default=0, help_text='竞技场胜率', verbose_name='竞技场胜率')),
                ('popularity_biaozhun', models.FloatField(default=0, help_text='标准占比', verbose_name='标准占比')),
                ('total_games_biaozhun', models.FloatField(default=0, help_text='标准总对局', verbose_name='标准总对局')),
                ('win_rate_biaozhun', models.FloatField(default=0, help_text='标准胜率', verbose_name='标准胜率')),
                ('Deck_UP_time', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='卡组对抗更新时间', max_length=100, null=True, verbose_name='卡组对抗更新时间')),
            ],
            options={
                'verbose_name': '各个职业在各个模式下的胜率',
                'verbose_name_plural': '各个职业在各个模式下的胜率',
            },
        ),
        migrations.AlterModelOptions(
            name='all_cards',
            options={'verbose_name': '所有狂野加标准卡牌卡牌,，来自hsreplay', 'verbose_name_plural': '所有狂野加标准卡牌卡牌,，来自hsreplay'},
        ),
    ]