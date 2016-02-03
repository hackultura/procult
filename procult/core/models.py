# -*- coding: utf-8 -*-

import re
import uuid
import os
from random import randint

from django.conf import settings
from django.db import models
from model_utils import Choices


def _generate_proposalnumber():
    return randint(1, 99999)

def _attachment_filepath(instance, filename):
  cpf = re.sub(r'\W', '_', instance.proposal.user.cpf)
  proposal = instance.proposal.number
  filename = re.sub(r'\s', '_', filename)
  path = "propostas/{cpf}/{proposal}/{filename}".format(
      cpf=cpf,
      proposal=proposal,
      filename=filename
  )
  return path


class Proposal(models.Model):
    STATUS_CHOICES = Choices(
        ('draft', "Rascunho"),
        ('sended', "Enviado"),
        ('analysis', "Em Análise"),
        ('approved', "Aprovado"),
        ('reproved', "Reprovado"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='proposals'
    )
    title = models.CharField(
        max_length=60
    )
    number = models.PositiveIntegerField(
        default=_generate_proposalnumber,
        editable=False
    )
    status = models.CharField(
        max_length=10,
        editable=False,
        default=STATUS_CHOICES.draft
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sended_at = models.DateTimeField(blank=True, null=True)

    @property
    def status_display(self):
        return Proposal.STATUS_CHOICES[self.status]


class AttachmentProposal(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    proposal = models.ForeignKey('Proposal', related_name='attachments')
    file = models.FileField(upload_to=_attachment_filepath)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(AttachmentProposal, self).delete(*args, **kwargs)
