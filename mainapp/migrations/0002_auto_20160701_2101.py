# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='employer_site',
            field=models.URLField(blank=True, verbose_name='Должность'),
        ),
    ]
