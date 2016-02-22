# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_ceac'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cpf', models.CharField(max_length=15, blank=True)),
                ('cnpj', models.CharField(max_length=20, blank=True)),
                ('ceac', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='ceac',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cnpj',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cpf',
        ),
        migrations.AddField(
            model_name='ente',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
