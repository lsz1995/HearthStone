# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-03 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0016_auto_20190803_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck_info',
            name='Deck_deck_list',
            field=models.CharField(default='', help_text='卡组', max_length=500, verbose_name='卡组'),
        ),
    ]
