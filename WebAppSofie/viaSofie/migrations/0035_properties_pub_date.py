# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 10:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0034_faq_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 17, 10, 37, 9, 655197, tzinfo=utc)),
            preserve_default=False,
        ),
    ]