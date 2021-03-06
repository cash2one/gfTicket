# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupportTicketSystem', '0033_project_need_completed_by_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='need_completed_by_admin',
        ),
        migrations.AddField(
            model_name='ticket',
            name='need_completed_by_admin',
            field=models.BooleanField(default=False, verbose_name='是否必须由管理员完成'),
        ),
        migrations.AddField(
            model_name='trouble',
            name='need_completed_by_admin',
            field=models.BooleanField(default=False, verbose_name='是否必须由管理员完成'),
        ),
    ]
