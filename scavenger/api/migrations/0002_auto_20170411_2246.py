# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Building'),
        ),
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Room'),
        ),
    ]
