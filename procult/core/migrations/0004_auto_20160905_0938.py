# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def port_models(apps, schema_editor):
    Proposal = apps.get_model('core', 'Proposal')
    Notice = apps.get_model('core', 'Notice')
    n = Notice()
    n.title = "Edital"
    n.description = "Edital info"
    n.save()

    for p in Proposal.objects.all():
        p.notice = n
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_proposaldate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=500)),
                ('is_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='notice',
            field=models.ForeignKey(related_name='proposals', to='core.Notice', null=True),
        ),
        migrations.RunPython(port_models),
    ]
