from django.contrib import admin
from .models import Proposal, AttachmentProposal


class ProposalAdmin(admin.ModelAdmin):
    pass


class AttachmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Proposal, ProposalAdmin)
admin.site.register(AttachmentProposal, AttachmentAdmin)
