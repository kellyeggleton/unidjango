# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant_details',
            name='Class_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vars.Classification'),
        ),
    ]
