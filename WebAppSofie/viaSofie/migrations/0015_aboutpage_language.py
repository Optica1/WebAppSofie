# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0014_auto_20160602_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='language',
            field=models.CharField(default='NL', max_length=20),
        ),
    ]
