# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('datecreated', models.DateTimeField()),
            ],
        ),
    ]
