# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='num_of_likes',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='num_of_posts',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
