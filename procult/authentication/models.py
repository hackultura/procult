# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django_extensions.db.fields import AutoSlugField
from .managers import UserManager, EntesManager


class User(AbstractBaseUser):
    ADMIN_REGIONS = (
        (0, "Não escolhido"),
        (1, "Brasília"),
        (2, "Gama"),
        (3, "Taguatinga"),
        (4, "Brazlândia"),
        (5, "Sobradinho"),
        (6, "Planaltina"),
        (7, "Paranoá"),
        (8, "Núcleo Bandeirante"),
        (9, "Ceilândia"),
        (10, "Guará"),
        (11, "Cruzeiro"),
        (12, "Samambaia"),
        (13, "Santa Maria"),
        (14, "São Sebastião"),
        (15, "Recanto das Emas"),
        (16, "Lago Sul"),
        (17, "Riacho Fundo"),
        (18, "Lago Norte"),
        (19, "Candangolândia"),
        (20, "Águas Claras"),
        (21, "Riacho Fundo II"),
        (22, "Sudoeste/Octogonal"),
        (23, "Varjão"),
        (24, "Park Way"),
        (25, "SCIA"),
        (26, "Sobradinho II"),
        (27, "Jardim Botânico"),
        (28, "Itapoã"),
        (29, "SIA"),
        (30, "Vicente Pires"),
        (31, "Fercal"),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=80, blank=False)
    gender = models.CharField(max_length=1, blank=True)
    age = models.IntegerField(default=0)
    admin_region = models.IntegerField(default=0, choices=ADMIN_REGIONS)
    slug = AutoSlugField(populate_from='name', overwrite=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    entes = EntesManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    @property
    def verbose_admin_region(self):
        return dict(self.ADMIN_REGIONS).get(self.admin_region, '')

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

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

    def __str__(self):
        return "{cpf}: {name}".format(cpf=self.cpf, name=self.user.name)
