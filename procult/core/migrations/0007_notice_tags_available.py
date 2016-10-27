# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def port_models(apps, schema_editor):
    ProposalTag = apps.get_model('core', 'ProposalTag')
    Notice = apps.get_model('core', 'Notice')
    tag = ProposalTag()
    tag.name = "Nenhuma"
    tag.save()

    for p in Notice.objects.all():
        p.tags_available.add(tag)
        p.save()

def reverse_port_models(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20161005_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='tags_available',
            field=models.ManyToManyField(to='core.ProposalTag'),
        ),
        migrations.RunPython(port_models, reverse_port_models),
    ]
