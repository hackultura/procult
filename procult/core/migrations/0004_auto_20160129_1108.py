# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_attachmentproposal_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 13, 8, 40, 369323, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='sended_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 13, 8, 46, 56966, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 13, 8, 49, 874055, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
