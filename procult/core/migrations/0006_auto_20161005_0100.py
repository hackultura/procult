# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_proposaldate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='tag',
            field=models.ForeignKey(related_name='proposals', to='core.ProposalTag', null=True),
        ),
    ]
