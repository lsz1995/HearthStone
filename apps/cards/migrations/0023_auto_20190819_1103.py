# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-19 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0022_auto_20190819_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_duikang',
            name='Group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card_group'),
        ),
    ]