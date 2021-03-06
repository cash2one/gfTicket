# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Document', '0007_auto_20160216_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentuser',
            name='db_manual_order',
            field=models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='db_manual_order',
            field=models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='db_manual_order',
            field=models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位'),
        ),
    ]
