# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-02 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_auto_20190802_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card_group',
            name='Group_recent3_average_hot',
        ),
        migrations.RemoveField(
            model_name='card_group',
            name='Group_recent3_average_win',
        ),
        migrations.AddField(
            model_name='card_group',
            name='Group_as_of_info',
            field=models.CharField(blank=True, default=0, help_text='原型对局信息更新时间', max_length=200, verbose_name='原型对局信息更新时间'),
        ),
        migrations.AlterField(
            model_name='card_group',
            name='Group_as_of',
            field=models.CharField(blank=True, default=0, help_text='原型加入时间', max_length=200, verbose_name='更新时间'),
        ),
    ]