# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viaSofie', '0021_auto_20160603_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name_plural': 'Over ons Pagina'},
        ),
        migrations.AlterModelOptions(
            name='aboutsofiepage',
            options={'verbose_name_plural': 'Over Sofie pagina'},
        ),
        migrations.AlterModelOptions(
            name='disclaimerpage',
            options={'verbose_name_plural': 'Disclaimer pagina'},
        ),
        migrations.AlterModelOptions(
            name='ebook',
            options={'verbose_name_plural': 'Ebooks'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name_plural': "Faq's"},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name_plural': 'Nieuwsbrief'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name_plural': 'Partners'},
        ),
        migrations.AlterModelOptions(
            name='privacypage',
            options={'verbose_name_plural': 'Privacy pagina'},
        ),
        migrations.AlterModelOptions(
            name='properties',
            options={'verbose_name_plural': 'Panden'},
        ),
    ]
