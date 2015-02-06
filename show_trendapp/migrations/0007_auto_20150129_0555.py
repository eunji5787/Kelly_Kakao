# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0006_auto_20150129_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_cnt',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_dd',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_hh',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_mm',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficperhour',
            name='traffic_yyyy',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
    ]
