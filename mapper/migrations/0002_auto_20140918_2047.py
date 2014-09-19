# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdbid',
            field=models.CharField(default="1234", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=1234, max_length=4),
            preserve_default=False,
        ),
    ]
