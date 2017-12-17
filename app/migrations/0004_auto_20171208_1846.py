# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-08 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171208_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='badge_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]