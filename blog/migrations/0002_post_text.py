# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='lol'),
            preserve_default=False,
        ),
    ]
