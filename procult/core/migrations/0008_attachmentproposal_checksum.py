# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_proposal_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachmentproposal',
            name='checksum',
            field=models.CharField(max_length=80, default='0000000000000000'),
            preserve_default=False,
        ),
    ]
