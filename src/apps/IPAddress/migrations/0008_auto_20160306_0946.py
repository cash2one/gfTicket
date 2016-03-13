# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 09:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPAddress', '0007_subnet_been_init'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='ping_last_success_delay',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='host',
            name='ping_last_success_fraction_loss',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='host',
            name='ping_last_success_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 9, 46, 57, 849)),
        ),
        migrations.AddField(
            model_name='host',
            name='ping_latest_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 9, 46, 56, 999848)),
        ),
    ]