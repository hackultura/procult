# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin_region',
            field=models.IntegerField(default=0, choices=[(0, b'N\xc3\xa3o escolhido'), (1, b'Bras\xc3\xadlia'), (2, b'Gama'), (3, b'Taguatinga'), (4, b'Brazl\xc3\xa2ndia'), (5, b'Sobradinho'), (6, b'Planaltina'), (7, b'Parano\xc3\xa1'), (8, b'N\xc3\xbacleo Bandeirante'), (9, b'Ceil\xc3\xa2ndia'), (10, b'Guar\xc3\xa1'), (11, b'Cruzeiro'), (12, b'Samambaia'), (13, b'Santa Maria'), (14, b'S\xc3\xa3o Sebasti\xc3\xa3o'), (15, b'Recanto das Emas'), (16, b'Lago Sul'), (17, b'Riacho Fundo'), (18, b'Lago Norte'), (19, b'Candangol\xc3\xa2ndia'), (20, b'\xc3\x81guas Claras'), (21, b'Riacho Fundo II'), (22, b'Sudoeste/Octogonal'), (23, b'Varj\xc3\xa3o'), (24, b'Park Way'), (25, b'SCIA'), (26, b'Sobradinho II'), (27, b'Jardim Bot\xc3\xa2nico'), (28, b'Itapo\xc3\xa3'), (29, b'SIA'), (30, b'Vicente Pires'), (31, b'Fercal')]),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=1, blank=True),
        ),
    ]
