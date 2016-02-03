# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator
from django_extensions.db.fields import AutoSlugField
from .managers import UserManager, EntesManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=80, blank=False)
    slug = AutoSlugField(populate_from='name', overwrite=True)
    cpf = models.CharField(max_length=15, blank=True)
    cnpj = models.CharField(max_length=20, blank=True)
    ceac = models.PositiveSmallIntegerField(
        blank=False,
        validators=[MaxValueValidator(9999)]
    )

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    entes = EntesManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split(' ')[0]
