# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yyyy', models.IntegerField(max_length=10, choices=[(b'0', b'all'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017')])),
                ('mm', models.IntegerField(max_length=10, choices=[(b'0', b'all'), (b'01', b'01'), (b'02', b'02'), (b'03', b'03'), (b'04', b'04'), (b'05', b'05'), (b'06', b'06'), (b'07', b'07'), (b'08', b'08'), (b'09', b'09'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12')])),
                ('dd', models.IntegerField(max_length=10, choices=[(b'0', b'all'), (b'01', b'01'), (b'02', b'02'), (b'03', b'03'), (b'04', b'04'), (b'05', b'05'), (b'06', b'06'), (b'07', b'07'), (b'08', b'08'), (b'09', b'09'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31')])),
                ('hh', models.IntegerField(max_length=10, choices=[(b'0', b'all'), (b'01', b'01'), (b'02', b'02'), (b'03', b'03'), (b'04', b'04'), (b'05', b'05'), (b'06', b'06'), (b'07', b'07'), (b'08', b'08'), (b'09', b'09'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24')])),
                ('fname', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
