# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-26 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(choices=[(0, '管理员'), (1, '卖家'), (2, '刷手'), (3, '代理')], default=1, help_text='账号类别: 0(管理员),1(卖家),2(刷手),3(代理)', verbose_name='账号类别'),
        ),
    ]
