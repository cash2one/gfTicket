# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 10:58
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Document', '0002_auto_20160212_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(default=0.0, verbose_name='顺位')),
                ('generic_permission', models.BooleanField(default=False, verbose_name='一般权限')),
                ('advanced_permission', models.BooleanField(default=False, verbose_name='高级权限')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='document_user', to=settings.AUTH_USER_MODEL, verbose_name='对应用户')),
            ],
            options={
                'verbose_name_plural': '文档系统权限',
                'verbose_name': '文档系统权限',
            },
        ),
    ]
