# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0009_auto_20150202_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficperhour',
            name='traffic_dd',
        ),
        migrations.RemoveField(
            model_name='trafficperhour',
            name='traffic_mm',
        ),
        migrations.RemoveField(
            model_name='trafficperhour',
            name='traffic_yyyy',
        ),
        migrations.RemoveField(
            model_name='urlperage',
            name='age_dd',
        ),
        migrations.RemoveField(
            model_name='urlperage',
            name='age_mm',
        ),
        migrations.RemoveField(
            model_name='urlperage',
            name='age_yyyy',
        ),
        migrations.AddField(
            model_name='urlperage',
            name='age_date',
            field=models.DateField(default=datetime.date(2015, 2, 2)),
            preserve_default=True,
        ),
    ]
