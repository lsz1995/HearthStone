# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-19 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0029_card_group_group_mas_of_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card_group',
            old_name='Group_mas_of_info',
            new_name='Group_as_of_info',
        ),
    ]