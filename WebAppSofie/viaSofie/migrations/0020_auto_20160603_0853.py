# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0019_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='eigendom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viaSofie.Properties'),
        ),
    ]
