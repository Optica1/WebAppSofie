# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0002_auto_20160513_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='buildingtype',
            field=models.CharField(choices=[('O', 'Open'), ('H', 'Half'), ('CL', 'Closed'), ('A', 'Appartment'), ('M', 'Mezzanine'), ('B', 'Bungalow'), ('CA', 'Caravan')], default='A', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='properties',
            name='heating_type',
            field=models.CharField(choices=[('E', 'Electric'), ('G', 'Gas'), ('F', 'Furnace'), ('H', 'Heat pump'), ('S', 'Special')], default='H', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='busnumber',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]