# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0010_auto_20160529_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='path',
            field=models.FilePathField(editable=False),
        ),
    ]
