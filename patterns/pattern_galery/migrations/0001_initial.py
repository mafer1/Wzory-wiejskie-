# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatternEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('visible', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_file', models.ImageField(upload_to='')),
                ('model_file', models.FileField(upload_to='')),
            ],
        ),
    ]