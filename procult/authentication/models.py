# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django_extensions.db.fields import AutoSlugField
from .managers import UserManager, EntesManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=80, blank=False)
    slug = AutoSlugField(populate_from='name', overwrite=True)

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


class Ente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=15, blank=True)
    cnpj = models.CharField(max_length=20, blank=True)
    ceac = models.PositiveSmallIntegerField(
        blank=False,
        validators=[MaxValueValidator(9999)]
    )

    objects = EntesManager()

    def clean(self):
        if self.cpf in [None, ''] and self.cnpj in [None, '']:
            raise ValidationError("É obrigatório o CPF ou CNPJ.")

        if Ente.objects.filter(cpf=self.cpf).exists():
            raise ValidationError({'cpf', "Esse CPF já foi usado no sistema."})

        if Ente.objects.filter(cnpj=self.cnpj).exists():
            raise ValidationError({'cnpj', "Esse CNPJ já foi usado no sistema."})

        if Ente.objects.filter(ceac=self.ceac).exists():
            raise ValidationError({'ceac', "Esse CEAC já foi usado no sistema."})

    def __str__(self):
        return "{cpf}: {name}".format(cpf=self.cpf, name=self.user.name)
