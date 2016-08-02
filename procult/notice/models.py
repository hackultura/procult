# -*- coding: utf-8 -*-

import uuid

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    uid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=80, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='subcategories', db_index=True)

    class MPTTMeta:
        db_table = "categories"
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Notice(models.Model):
    uid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField('notice.Category',
                                        related_name='categories')
    resume = models.TextField()
    notice_url = models.URLField()
    start_publication = models.DateTimeField()
    end_publication = models.DateTimeField()

    class Meta:
        db_table = "notices"

    def __str__(self):
        return self.name
