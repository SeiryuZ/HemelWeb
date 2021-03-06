# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 23:04
from __future__ import unicode_literals

import core.fields
from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20160701_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='configuration_file',
            field=core.fields.ContentTypeRestrictedFileField(blank=True, upload_to=jobs.models.job_directory_path, verbose_name=b'Config (.xml)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='input_file',
            field=core.fields.ContentTypeRestrictedFileField(blank=True, upload_to=jobs.models.job_directory_path, verbose_name=b'Input (.gmy)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='profile_file',
            field=core.fields.ContentTypeRestrictedFileField(blank=True, upload_to=jobs.models.job_directory_path, verbose_name=b'Profile file (.pr2)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.IntegerField(choices=[(1, b'Added'), (2, b'Queued'), (10, b'Running'), (3, b'Done'), (0, b'Failed'), (4, b'Preprocessing'), (5, b'Previous Job on S3')], default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='stl_file',
            field=core.fields.ContentTypeRestrictedFileField(blank=True, upload_to=jobs.models.job_directory_path, verbose_name=b'Geometry file (.stl)'),
        ),
    ]
