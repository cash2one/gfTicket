# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPAddress', '0031_remove_host_ping_stdout'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='ping_stdout',
            field=models.TextField(default='=.=!', verbose_name='Ping输出'),
        ),
    ]
