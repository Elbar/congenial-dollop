# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-04 18:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20180304_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='until',
            field=models.DateField(default=datetime.datetime(2018, 3, 25, 18, 3, 54, 842419)),
        ),
    ]