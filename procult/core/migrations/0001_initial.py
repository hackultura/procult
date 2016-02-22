# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import procult.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentProposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('file', models.FileField(upload_to=procult.core.models._attachment_filepath)),
                ('checksum', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('number', models.PositiveIntegerField(default=procult.core.models._generate_proposalnumber, editable=False)),
                ('status', models.CharField(default='draft', max_length=10, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sended_at', models.DateTimeField(null=True, blank=True)),
                ('ente', models.ForeignKey(to='authentication.Ente', related_name='proposals')),
            ],
        ),
        migrations.AddField(
            model_name='attachmentproposal',
            name='proposal',
            field=models.ForeignKey(to='core.Proposal', related_name='attachments'),
        ),
    ]
