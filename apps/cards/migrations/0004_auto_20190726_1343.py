# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-26 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20190726_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_cards',
            name='card_id',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='hsreplay_dbf_ID'),
        ),
    ]
