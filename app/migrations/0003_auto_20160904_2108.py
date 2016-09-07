# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_item_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='todo_list',
        ),
        migrations.AddField(
            model_name='item',
            name='state',
            field=models.IntegerField(default=1, choices=[(1, b'Low'), (2, b'Normal'), (3, b'High')]),
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
