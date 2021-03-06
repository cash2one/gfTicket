# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Equipment', '0005_auto_20160219_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentbrand',
            name='db_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='激活'),
        ),
        migrations.AlterField(
            model_name='equipmentmodel',
            name='db_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='激活'),
        ),
        migrations.AlterField(
            model_name='equipmenttype',
            name='db_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='激活'),
        ),
    ]
