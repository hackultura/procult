# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160905_0938'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProposalDate',
        ),
    ]
