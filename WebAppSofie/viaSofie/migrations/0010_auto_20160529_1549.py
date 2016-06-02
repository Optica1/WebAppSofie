# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0009_newsletter_partner_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='dossierStatus',
            field=models.CharField(choices=[('R', 'Registered'), ('H', 'Handled')], default='R', max_length=1),
        ),
    ]