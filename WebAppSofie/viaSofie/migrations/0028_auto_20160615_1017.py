# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 10:17
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0027_auto_20160612_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertypictures',
            name='property_id',
        ),
        migrations.AddField(
            model_name='partner',
            name='photo',
            field=models.ImageField(default='/media/partner.jpg', storage=django.core.files.storage.FileSystemStorage(), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=b''),
        ),
        migrations.DeleteModel(
            name='PropertyPictures',
        ),
    ]
