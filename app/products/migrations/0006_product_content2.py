# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-17 14:47
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20171217_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content2',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=b''),
        ),
    ]
