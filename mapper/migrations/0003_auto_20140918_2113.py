# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0002_auto_20140918_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbid',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(max_length=4, null=True),
        ),
    ]
