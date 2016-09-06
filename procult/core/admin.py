from django.contrib import admin
from .models import Proposal, AttachmentProposal
from .forms import ProposalForm

class AttachmentAdmin(admin.ModelAdmin):
    pass


class AttachmentInline(admin.TabularInline):
    readonly_fields=('checksum',)
    model = AttachmentProposal


class ProposalAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline,]
    form = ProposalForm

#admin.site.register(Proposal, ProposalAdmin)
#admin.site.register(AttachmentProposal, AttachmentAdmin)
