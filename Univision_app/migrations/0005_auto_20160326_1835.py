# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Univision_app', '0004_auto_20160326_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
