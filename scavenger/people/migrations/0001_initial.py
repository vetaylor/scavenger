# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('prefix', models.CharField(blank=True, max_length=3)),
                ('groups', models.ManyToManyField(to='people.Group')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
    ]
