# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170520_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giveaway',
            name='price',
        ),
    ]