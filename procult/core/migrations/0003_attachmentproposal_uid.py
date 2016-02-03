# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160128_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachmentproposal',
            name='uid',
            field=models.UUIDField(editable=False, default=uuid.uuid4),
        ),
    ]
