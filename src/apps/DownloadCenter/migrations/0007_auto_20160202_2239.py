# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('DownloadCenter', '0006_auto_20160202_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='orig_file',
            field=models.FileField(help_text='选择一个文件并上传', upload_to="123", verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='orig_file',
            field=models.FileField(help_text='选择一个文件并上传', upload_to="123", verbose_name='文件'),
        ),
    ]