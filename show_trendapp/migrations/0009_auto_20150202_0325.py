# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0008_auto_20150129_0610'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Url_db',
        ),
        migrations.AddField(
            model_name='trafficperhour',
            name='traffic_date',
            field=models.DateField(default=datetime.date(2015, 2, 2)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trendingurl',
            name='trend_hh',
            field=models.IntegerField(max_length=10, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (0, 24)]),
            preserve_default=True,
        ),
    ]
