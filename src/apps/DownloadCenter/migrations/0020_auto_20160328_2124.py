# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DownloadCenter', '0019_auto_20160328_2123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesssoftware',
            options={'ordering': ['-db_created'], 'verbose_name': '业务软件', 'verbose_name_plural': '业务软件'},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['-db_created'], 'verbose_name': '驱动程序', 'verbose_name_plural': '驱动程序'},
        ),
    ]
