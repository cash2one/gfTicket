# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DownloadCenter', '0018_auto_20160306_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'ordering': ['-db_created'], 'verbose_name': '附件', 'verbose_name_plural': '附件'},
        ),
    ]
