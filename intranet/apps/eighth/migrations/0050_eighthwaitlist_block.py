# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eighth', '0049_auto_20170106_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='eighthwaitlist',
            name='block',
            field=models.ForeignKey(default=3155, on_delete=django.db.models.deletion.CASCADE, to='eighth.EighthBlock'),
            preserve_default=False,),
    ]
