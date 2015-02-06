# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0003_auto_20150128_0129'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ManageUrl',
        ),
        migrations.AddField(
            model_name='trendingurl',
            name='manage_url',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
