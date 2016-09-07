# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160904_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='state',
            field=models.IntegerField(default=1, choices=[(1, b'Todo'), (2, b'Doing'), (3, b'Done')]),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(unique=True, max_length=250),
        ),
    ]
