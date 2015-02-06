# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0007_auto_20150129_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendingurl',
            name='timespan_per_hour',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trendingurl',
            name='trend_dd',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trendingurl',
            name='trend_hh',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trendingurl',
            name='trend_mm',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trendingurl',
            name='trend_title',
            field=models.IntegerField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trendingurl',
            name='trend_url_cnt',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trendingurl',
            name='trend_yyyy',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urlperage',
            name='age_dd',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urlperage',
            name='age_mm',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urlperage',
            name='age_url_cnt',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urlperage',
            name='age_yyyy',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
    ]
