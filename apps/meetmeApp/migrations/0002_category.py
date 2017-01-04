# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meetmeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
            ],
        ),
    ]