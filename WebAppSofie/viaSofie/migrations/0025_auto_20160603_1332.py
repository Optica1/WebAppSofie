# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0024_delete_aboutsofiepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='title_dutch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='properties',
            name='title_french',
            field=models.CharField(max_length=100),
        ),
    ]
