# -*- coding: utf-8 -*-

from django.db.models import Q
from django.db import models

class ProposalManager(models.Manager):
    def sended(self):
        return self.filter(status=self.model.STATUS_CHOICES.sended)

    def approved(self):
        return self.filter(status=self.model.STATUS_CHOICES.approved)

    def reproved(self):
        return self.filter(status=self.model.STATUS_CHOICES.reproved)

    def canceled(self):
        return self.filter(status=self.model.STATUS_CHOICES.canceled)

    def last_sended(self, size=5):
        return self.sended()[:size]

    def last_analyzed(self, size=5):
        query = Q(status=self.model.STATUS_CHOICES.approved) & Q(
            status=self.model.STATUS_CHOICES.reproved)
        return self.filter(query)[:size]
