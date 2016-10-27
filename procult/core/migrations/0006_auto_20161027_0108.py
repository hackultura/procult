# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from procult.core.utils import _generate_proposalnumber

def port_models(apps, schema_editor):
    Proposal = apps.get_model('core', 'Proposal')

    for p in Proposal.objects.all():
    	# if duplicated number, generate a new unique number
        if len(Proposal.objects.filter(number=p.number)) > 1:
        	p.number = _generate_proposalnumber()
        	p.save()

def reverse_port_models(apps, schema_editor):
	pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_proposaldate'),
    ]

    operations = [
        migrations.RunPython(port_models, reverse_port_models),
    ]
