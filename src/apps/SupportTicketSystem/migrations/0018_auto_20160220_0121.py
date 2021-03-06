# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 01:21
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SupportTicketSystem', '0017_auto_20160220_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticketsystemuser',
            name='db_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='激活'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='db_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='激活'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='db_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='激活'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='detail',
            field=models.TextField(blank=True, help_text='设备序列号、用户帐号、任何其他重要信息', null=True, verbose_name='详细信息'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='relevant_business',
            field=models.ManyToManyField(blank=True, help_text='涉及的业务系统，没有请留空', related_name='relevant_ticket', to='BusinessSystem.System', verbose_name='涉及系统'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='relevant_equipment',
            field=models.ManyToManyField(blank=True, help_text='涉及的硬件设备类型，请尽量准确，没有请留空', related_name='relevant_ticket', to='Equipment.EquipmentModel', verbose_name='涉及硬件'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='scheduled_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='默认为当前时间立即开始', verbose_name='计划开始日期'),
        ),
        migrations.AlterField(
            model_name='trouble',
            name='db_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='激活'),
        ),
    ]
