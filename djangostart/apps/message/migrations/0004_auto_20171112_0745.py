# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20171112_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_key',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='主键'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='用户名'),
        ),
    ]
