# -*- coding: utf-8 -*-

import re
import uuid
import os
import shutil
import hashlib
from random import randint

from django.dispatch.dispatcher import receiver
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from model_utils import Choices
from .utils import normalize_text
from .signals import remove_proposal_file, remove_proposal_folder

def _generate_proposalnumber():
    return randint(1, 99999)

def _attachment_filepath(instance, filename):
  cpf = re.sub(r'\W', '_', instance.proposal.user.cpf)
  proposal = instance.proposal.number
  filename = normalize_text(filename)
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

    def delete(self, *args, **kwargs):
        remove_proposal_folder.send(sender=self.__class__,
                                    instance=self,
                                    user=self.user)
        super(Proposal, self).delete(*args, **kwargs)


class AttachmentProposal(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    proposal = models.ForeignKey('Proposal', on_delete=models.CASCADE,
                                 related_name='attachments')
    file = models.FileField(upload_to=_attachment_filepath)
    checksum = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        remove_proposal_file.send(sender=self.__class__, instance=self)
        super(AttachmentProposal, self).delete(*args, **kwargs)


# Signals
@receiver(pre_save, sender=AttachmentProposal)
def generate_checksum(sender, instance, **kwargs):
    instance.checksum = hashlib.md5(instance.file.read()).hexdigest()


@receiver(remove_proposal_file)
def delete_proposal_file(sender, instance, **kwargs):
    file_path = os.path.join(settings.MEDIA_ROOT, instance.file.name)
    if os.path.exists(file_path):
        os.remove(os.path.join(settings.MEDIA_ROOT, instance.file.name))


@receiver(remove_proposal_folder)
def delete_proposal_folder(sender, instance, user, **kwargs):
    number = str(instance.number)
    cpf = re.sub(r'\W', '_', user.cpf)
    path = "propostas/{0}/{1}".format(cpf, number)
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, path))
