# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 4, 20, 55, 12, 754969)),
            preserve_default=False,
        ),
    ]
