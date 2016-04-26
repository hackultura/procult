# -*- coding: utf-8 -*-

from import_export import resources, fields
from .models import Proposal


class ProposalResource(resources.ModelResource):
    """
    Resource do modelo de Propostas para
    exportar nos formatos desejados
    """
    numero = fields.Field()
    artista = fields.Field()
    projeto = fields.Field()
    criado_em = fields.Field()
    enviado_em = fields.Field()

    class Meta:
        model = Proposal
        fields = ("numero", "artista", "projeto",
                  "criado_em", "enviado_em",)
        export_order = ("numero", "artista", "projeto",
                        "criado_em", "enviado_em",)
        exclude = ("id", "number", "ente", "title",
                   "status", "created_at", "sended_at", "updated_at",)

    def get_queryset(self):
        return Proposal.objects.filter(status=Proposal.STATUS_CHOICES.sended)

    def dehydrate_numero(self, proposal):
        return proposal.number

    def dehydrate_artista(self, proposal):
        return proposal.ente.user.name

    def dehydrate_projeto(self, proposal):
        return proposal.title

    def dehydrate_criado_em(self, proposal):
        return proposal.created_at.strftime("%d/%m/%Y %H:%M:%S")

    def dehydrate_enviado_em(self, proposal):
        return proposal.sended_at.strftime("%d/%m/%Y %H:%M:%S")