# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPAddress', '0022_auto_20160318_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='ping_stdout',
            field=models.BinaryField(blank=True, null=True, verbose_name='Ping输出'),
        ),
    ]
