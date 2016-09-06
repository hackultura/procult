# -*- coding: utf-8 -*-

from django.db.models import Q
from django.db import models

DASHBOARD_PAGE_SIZE = 5


class ProposalManager(models.Manager):
    def drafted(self):
        return self.filter(status=self.model.STATUS_CHOICES.draft)

    def sended(self):
        return self.filter(status=self.model.STATUS_CHOICES.sended)

    def approved(self):
        return self.filter(status=self.model.STATUS_CHOICES.approved)

    def reproved(self):
        return self.filter(status=self.model.STATUS_CHOICES.reproved)

    def canceled(self):
        return self.filter(status=self.model.STATUS_CHOICES.canceled)

    def last_sended(self, notice_id=None, size=DASHBOARD_PAGE_SIZE):
        if notice_id:
            return self.sended().filter(notice=notice_id)[:size]

        return self.sended()[:size]

    def last_analyzed(self, notice_id=None, size=DASHBOARD_PAGE_SIZE):
        query = Q(status=self.model.STATUS_CHOICES.approved) & Q(
            status=self.model.STATUS_CHOICES.reproved)
        if notice_id:
            return self.filter(query).filter(notice=notice_id)[:size]

        return self.filter(query)[:size]

