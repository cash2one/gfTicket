# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('IPAddress', '0006_auto_20160220_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='subnet',
            name='been_init',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
