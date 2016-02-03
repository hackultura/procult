# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Usuario precisa de um email valido.")

        if not kwargs.get('name'):
            raise ValueError("Usuario precisa do nome completo.")

        user = self.model(
            email=self.normalize_email(email),
            name=kwargs.get('name')
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_admin = True
        user.save()

        return user

    def admins(self):
        return self.exclude(is_admin=False)


class EntesManager(models.Manager):
    def get_queryset(self):
        return super(EntesManager, self).get_queryset().exclude(
            cpf__exact='', cnpj__exact='')

    def with_cpf(self):
        return self.exclude(cpf__exact='')

    def with_cnpj(self):
        return self.exclude(cnpj__exact='')
