# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManageUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manage_url', models.URLField(default=b'', max_length=500, blank=True)),
                ('manage_title', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrafficPerHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('traffic_yyyy', models.CharField(max_length=10)),
                ('traffic_mm', models.CharField(max_length=10)),
                ('traffic_dd', models.CharField(max_length=10)),
                ('traffic_hh', models.CharField(max_length=10)),
                ('traffic_cnt', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrendingUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trend_yyyy', models.CharField(max_length=10)),
                ('trend_mm', models.CharField(max_length=10)),
                ('trend_dd', models.CharField(max_length=10)),
                ('trend_hh', models.CharField(max_length=10)),
                ('trend_url', models.URLField(default=b'', max_length=500, blank=True)),
                ('trend_title', models.CharField(max_length=100)),
                ('trend_url_cnt', models.CharField(max_length=10)),
                ('timespan_per_hour', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UrlPerAge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age_yyyy', models.CharField(max_length=10)),
                ('age_mm', models.CharField(max_length=10)),
                ('age_dd', models.CharField(max_length=10)),
                ('age_url', models.URLField(default=b'', max_length=500, blank=True)),
                ('age_title', models.CharField(max_length=100)),
                ('age_url_cnt', models.CharField(max_length=10)),
                ('under_tf', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='url_db',
            name='id',
        ),
        migrations.AlterField(
            model_name='url_db',
            name='dd',
            field=models.CharField(max_length=10, choices=[(b'01', b'1'), (b'02', b'2'), (b'03', b'3'), (b'04', b'4'), (b'05', b'5'), (b'06', b'6'), (b'07', b'7'), (b'08', b'8'), (b'09', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url_db',
            name='fname',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url_db',
            name='hh',
            field=models.CharField(max_length=10, choices=[(b'01', b'1'), (b'02', b'2'), (b'03', b'3'), (b'04', b'4'), (b'05', b'5'), (b'06', b'6'), (b'07', b'7'), (b'08', b'8'), (b'09', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'00', b'24')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url_db',
            name='mm',
            field=models.CharField(max_length=10, choices=[(b'01', b'1'), (b'02', b'2'), (b'03', b'3'), (b'04', b'4'), (b'05', b'5'), (b'06', b'6'), (b'07', b'7'), (b'08', b'8'), (b'09', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url_db',
            name='yyyy',
            field=models.CharField(max_length=10, choices=[(b'14', b'2014'), (b'15', b'2015'), (b'16', b'2016'), (b'17', b'2017')]),
            preserve_default=True,
        ),
    ]
