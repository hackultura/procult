from django.contrib import admin
from .models import Proposal, AttachmentProposal


class AttachmentAdmin(admin.ModelAdmin):
    pass


class AttachmentInline(admin.TabularInline):
    readonly_fields=('checksum',)
    model = AttachmentProposal


class ProposalAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline,]


admin.site.register(Proposal, ProposalAdmin)
admin.site.register(AttachmentProposal, AttachmentAdmin)
