# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160907_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_likes',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
