# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import procult.core.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentProposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('file', models.FileField(upload_to=procult.core.models._attachment_filepath)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number', models.PositiveIntegerField(editable=False, default=procult.core.models._generate_proposalnumber)),
                ('ceac', models.PositiveSmallIntegerField()),
                ('status', models.CharField(editable=False, default='draft', max_length=10)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='proposals')),
            ],
        ),
        migrations.AddField(
            model_name='attachmentproposal',
            name='proposal',
            field=models.ForeignKey(to='core.Proposal', related_name='attachments'),
        ),
    ]
