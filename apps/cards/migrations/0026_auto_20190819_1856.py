# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-19 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0025_auto_20190819_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_pct',
            name='Group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card_group', verbose_name='原型ID'),
        ),
    ]