# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-09 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0020_player_class_zhiye_zhongwen'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck_info',
            name='cost_total',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='卡组费用'),
        ),
    ]
