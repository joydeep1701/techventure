# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-10 07:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0008_auto_20170910_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 10, 7, 1, 45, 125663, tzinfo=utc)),
        ),
    ]