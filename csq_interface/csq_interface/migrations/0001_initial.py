# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 16:44
from __future__ import unicode_literals

import csq_interface.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile', models.FileField(upload_to=csq_interface.models.data_file_name)),
                ('datatimestamp', models.DateTimeField()),
                ('configfile', models.FileField(upload_to=csq_interface.models.config_file_name)),
                ('configtimestamp', models.DateTimeField()),
                ('graphfile', models.FileField(upload_to=csq_interface.models.graph_file_name)),
                ('graphtimestamp', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
