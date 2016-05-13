# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viaSofie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('path', models.FilePathField()),
                ('language', models.CharField(max_length=3)),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EbookRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('send', models.BooleanField()),
                ('ebook_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viaSofie.Ebook')),
            ],
        ),
        migrations.CreateModel(
            name='PlanningInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voorkooprecht', models.BooleanField()),
                ('bouwvergunning', models.BooleanField()),
                ('dagvaarding', models.BooleanField()),
                ('verkaveling', models.BooleanField()),
                ('juridische_beslissing', models.BooleanField()),
                ('co2_emission', models.CharField(max_length=5)),
                ('epc', models.CharField(max_length=10)),
                ('unique_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('housenumber', models.CharField(max_length=4)),
                ('busnumber', models.CharField(max_length=3)),
                ('postalcode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=8)),
                ('sale', models.BooleanField()),
                ('area', models.CharField(max_length=10)),
                ('livingarea', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=4)),
                ('rateable_value', models.CharField(max_length=8)),
                ('description', models.TextField()),
                ('energy_label', models.CharField(max_length=5)),
                ('extra_information', models.TextField()),
                ('available', models.BooleanField()),
                ('sold', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField()),
                ('available', models.BooleanField()),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viaSofie.Properties')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField()),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viaSofie.Properties')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='userdetails',
            name='busnumber',
            field=models.CharField(blank=True, default='a', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='city',
            field=models.CharField(default='Antwerpen', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='country',
            field=models.CharField(default='Belgium', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='housenumber',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='postalcode',
            field=models.CharField(default=2000, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetails',
            name='street',
            field=models.CharField(default='Meistraat', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='text',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viaSofie.Room')),
                ('bath_type', models.CharField(max_length=15)),
            ],
            bases=('viaSofie.room',),
        ),
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viaSofie.Room')),
            ],
            bases=('viaSofie.room',),
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viaSofie.Room')),
            ],
            bases=('viaSofie.room',),
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viaSofie.Room')),
            ],
            bases=('viaSofie.room',),
        ),
        migrations.CreateModel(
            name='Livingroom',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viaSofie.Room')),
            ],
            bases=('viaSofie.room',),
        ),
        migrations.CreateModel(
            name='Storageroom',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viaSofie.Room')),
            ],
            bases=('viaSofie.room',),
        ),
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viaSofie.Room')),
            ],
            bases=('viaSofie.room',),
        ),
        migrations.AddField(
            model_name='room',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viaSofie.Properties'),
        ),
        migrations.AddField(
            model_name='planninginfo',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viaSofie.Properties'),
        ),
    ]
