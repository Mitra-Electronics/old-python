# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-07 13:19
from __future__ import unicode_literals

import annoying.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silver', '0046_auto_20180214_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='meta',
            field=annoying.fields.JSONField(blank=True, default={}, null=True),
        ),
    ]
