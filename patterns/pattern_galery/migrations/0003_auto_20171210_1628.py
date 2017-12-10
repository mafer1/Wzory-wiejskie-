# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern_galery', '0002_patternentry_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patternentry',
            name='image_file',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='patternentry',
            name='model_file',
            field=models.FileField(upload_to='pattern_zips/'),
        ),
    ]