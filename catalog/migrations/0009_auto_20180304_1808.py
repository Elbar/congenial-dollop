# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-04 18:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180304_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='until',
            field=models.DateField(default=datetime.datetime(2018, 3, 25, 18, 8, 2, 812018)),
        ),
    ]
