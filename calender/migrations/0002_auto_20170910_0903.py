# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-10 03:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calender',
            old_name='deleted',
            new_name='completed',
        ),
        migrations.AlterField(
            model_name='calender',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 10, 9, 3, 3, 58688, tzinfo=utc)),
        ),
    ]
