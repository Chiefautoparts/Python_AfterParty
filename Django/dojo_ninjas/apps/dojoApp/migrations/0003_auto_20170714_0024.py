# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-14 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojoApp', '0002_auto_20170713_0720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninja',
            old_name='dojo',
            new_name='name',
        ),
    ]
