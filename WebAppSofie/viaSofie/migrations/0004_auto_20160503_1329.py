# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0003_auto_20160503_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='text',
            field=models.TextField(max_length=1024),
        ),
    ]
