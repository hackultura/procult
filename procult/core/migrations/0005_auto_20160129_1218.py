# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160129_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='sended_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
