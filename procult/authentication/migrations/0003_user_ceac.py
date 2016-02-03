# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ceac',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999)]),
            preserve_default=False,
        ),
    ]
