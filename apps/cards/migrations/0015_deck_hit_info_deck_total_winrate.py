# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-02 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0014_deck_info_deck_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck_hit_info',
            name='Deck_total_winrate',
            field=models.FloatField(default=0, help_text='总体胜率', verbose_name='总体胜率'),
        ),
    ]