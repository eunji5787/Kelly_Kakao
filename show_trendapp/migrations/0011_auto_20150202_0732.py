# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0010_auto_20150202_0508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trendingurl',
            name='trend_dd',
        ),
        migrations.RemoveField(
            model_name='trendingurl',
            name='trend_mm',
        ),
        migrations.RemoveField(
            model_name='trendingurl',
            name='trend_yyyy',
        ),
        migrations.AddField(
            model_name='trendingurl',
            name='trend_date',
            field=models.DateField(default=datetime.date(2015, 2, 2)),
            preserve_default=True,
        ),
    ]
