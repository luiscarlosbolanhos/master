# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(blank='true', max_length=200),
        ),
    ]