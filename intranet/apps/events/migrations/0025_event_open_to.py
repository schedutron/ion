# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-08 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_auto_20170307_2037_squashed_0025_auto_20170307_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='open_to',
            field=models.CharField(choices=[('everyone', 'Everyone'), ('students', 'Students'), ('parents', 'Parents')], default='everyone',
                                   max_length=10),),
    ]
