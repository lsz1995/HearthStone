# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-05 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0017_auto_20190803_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_class',
            name='zhiye_image',
            field=models.CharField(default='', max_length=500, verbose_name='图片'),
        ),
    ]