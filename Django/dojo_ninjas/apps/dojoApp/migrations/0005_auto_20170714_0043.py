# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-14 00:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojoApp', '0004_auto_20170714_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninja',
            old_name='name',
            new_name='dojo',
        ),
    ]
