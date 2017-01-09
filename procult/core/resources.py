# -*- coding: utf-8 -*-
from django.utils import timezone

from import_export import resources, fields
from .models import Proposal


class ProposalResource(resources.ModelResource):
    """
    Resource do modelo de Propostas para
    exportar nos formatos desejados
    """
    estado = fields.Field()
    numero = fields.Field()
    pasta_proposta = fields.Field()
    artista = fields.Field()
    documento = fields.Field()
    projeto = fields.Field()
    criado_em = fields.Field()
    enviado_em = fields.Field()
    edital = fields.Field()
    numero_edital = fields.Field()
    genero = fields.Field()
    idade = fields.Field()
    regiao_administrativa = fields.Field()

    class Meta:
        model = Proposal
        fields = ("estado", "numero", "pasta_proposta", "artista", "documento", "projeto",
                  "criado_em", "enviado_em", "edital", "numero_edital", "genero", "idade", "regiao_administrativa")
        export_order = ("estado", "numero", "pasta_proposta", "artista","projeto",
                        "documento", "criado_em", "enviado_em", "edital", "numero_edital", "genero", "idade", "regiao_administrativa")
        exclude = ("id", "number", "ente", "title",
                   "status", "created_at", "sended_at", "updated_at", "notice")

    def get_queryset(self):
        return Proposal.objects.all()

    def dehydrate_estado(self, proposal):
        return proposal.status_display

    def dehydrate_numero_edital(self, proposal):
        return proposal.notice.id

    def dehydrate_edital(self, proposal):
        return proposal.notice.title

    def dehydrate_numero(self, proposal):
        return proposal.id

    def dehydrate_pasta_proposta(self, proposal):
        return proposal.number

    def dehydrate_artista(self, proposal):
        return proposal.ente.user.name

    def dehydrate_documento(self, proposal):
        return proposal.ente.cpf or proposal.ente.cnpj

    def dehydrate_projeto(self, proposal):
        return proposal.title

    def dehydrate_criado_em(self, proposal):
        return proposal.created_at.astimezone(timezone.get_current_timezone()).strftime("%d/%m/%Y %H:%M:%S")

    def dehydrate_enviado_em(self, proposal):
        if proposal.sended_at:
            return proposal.sended_at.astimezone(timezone.get_current_timezone()).strftime("%d/%m/%Y %H:%M:%S")
        else:
            return ""

    def dehydrate_genero(self, proposal):
        return proposal.ente.user.gender

    def dehydrate_idade(self, proposal):
        return proposal.ente.user.age

    def dehydrate_regiao_administrativa(self, proposal):
        return proposal.ente.user.verbose_admin_region
