# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_proposal_ceac'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='title',
            field=models.CharField(max_length=60, default=''),
            preserve_default=False,
        ),
    ]
