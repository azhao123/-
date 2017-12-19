# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-17 13:35
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('price', models.IntegerField(verbose_name='\u4ef7\u683c')),
                ('point', models.IntegerField(verbose_name='\u5546\u54c1\u79ef\u5206')),
                ('nicimage', models.ImageField(default=b'product_nic/default.png', upload_to=b'product_nic/%Y/%m', verbose_name='\u5546\u54c1\u7f29\u7565\u56fe')),
                ('image', models.ImageField(default=b'product/default.png', upload_to=b'product/%Y/%m', verbose_name='\u5546\u54c1\u56fe\u7247')),
                ('image2', models.ImageField(default=b'product/default.png', upload_to=b'product/%Y/%m', verbose_name='\u5546\u54c1\u56fe\u72472')),
                ('image3', models.ImageField(default=b'product/default.png', upload_to=b'product/%Y/%m', verbose_name='\u5546\u54c1\u56fe\u72473')),
                ('image4', models.ImageField(default=b'product/default.png', upload_to=b'product/%Y/%m', verbose_name='\u5546\u54c1\u56fe\u72474')),
                ('image5', models.ImageField(default=b'product/default.png', upload_to=b'product/%Y/%m', verbose_name='\u5546\u54c1\u56fe\u72475')),
                ('des', models.CharField(max_length=500, verbose_name='\u5546\u54c1\u8be6\u7ec6\u63cf\u8ff0')),
                ('add_time', models.DateTimeField(verbose_name='\u5546\u54c1\u4e0a\u67b6\u65f6\u95f4')),
                ('sell_nums', models.IntegerField(verbose_name='\u5546\u54c1\u9500\u91cf')),
                ('ku_cun', models.IntegerField(verbose_name='\u5546\u54c1\u5e93\u5b58')),
                ('comment', models.CharField(default=b'', max_length=500, verbose_name='\u8bc4\u8bba')),
                ('tag', models.IntegerField(choices=[(1, '\u793c\u54c1\u7bb1\u5305'), (2, '\u5bb6\u5c45\u5bb6\u88c5'), (3, '\u6570\u7801\u529e\u516c'), (4, '\u670d\u9970\u978b\u5e3d'), (5, '\u5bb6\u7528\u7535\u5668'), (6, '\u4e2a\u62a4\u5316\u5986'), (7, '\u53a8\u623f\u9910\u996e'), (8, '\u73e0\u5b9d\u624b\u8868'), (9, '\u8fd0\u52a8\u5065\u5eb7')], default=1, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb')),
                ('brand', models.IntegerField(choices=[(1, b'addids'), (2, b'lining'), (3, b'baidu')], default=1, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
    ]
