# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-10 06:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0006_auto_20170910_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 10, 6, 59, 56, 974773, tzinfo=utc)),
        ),
    ]
