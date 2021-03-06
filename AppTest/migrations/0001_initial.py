# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameName', models.CharField(max_length=100)),
                ('gameCode', models.CharField(max_length=20)),
                ('account', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('accUser', models.CharField(max_length=50)),
                ('packageName', models.CharField(max_length=50)),
                ('devIp', models.CharField(max_length=50)),
                ('devAccount', models.CharField(max_length=50)),
                ('devPassword', models.CharField(max_length=50)),
                ('accountType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameName', models.CharField(max_length=100)),
                ('gameCode', models.CharField(max_length=20)),
                ('gameType', models.CharField(max_length=20)),
                ('parentGame', models.CharField(max_length=20)),
                ('tort', models.CharField(max_length=20)),
                ('versionName', models.CharField(max_length=30)),
                ('engine', models.CharField(max_length=30)),
            ],
        ),
    ]
