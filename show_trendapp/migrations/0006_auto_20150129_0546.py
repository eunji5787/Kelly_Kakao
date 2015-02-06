# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0005_auto_20150129_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_cnt',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_dd',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_hh',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_mm',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_yyyy',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
