# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 03:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20171112_0336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户留言信息'},
        ),
    ]