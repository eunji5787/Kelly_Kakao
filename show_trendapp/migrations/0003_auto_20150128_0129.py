# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_trendapp', '0002_auto_20150127_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlperage',
            old_name='under_tf',
            new_name='over_tf',
        ),
    ]
