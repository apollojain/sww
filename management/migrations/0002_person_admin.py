# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
