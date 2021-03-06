# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 09:46
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160924_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='introduction',
            field=models.CharField(max_length=150, null=True, validators=[blog.validators.badwords]),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_body',
            field=models.TextField(default='Cuerpo del post', validators=[blog.validators.badwords]),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='Titulo', max_length=50, validators=[blog.validators.badwords]),
        ),
    ]
