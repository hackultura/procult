# -*- coding: utf-8 -*-

import re

from django.core.files.uploadedfile import UploadedFile
from rest_framework import serializers
from .models import Proposal, AttachmentProposal


class ProposalUploadSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(format='hex', required=False)
    file = serializers.FileField(max_length=255, write_only=True)
    file = serializers.SerializerMethodField()
    filename = serializers.SerializerMethodField()
    class Meta:
        model = AttachmentProposal
        fields = ('file', 'uid', 'checksum', 'filename',)
        read_only_fields = ('uuid', 'file', 'created_at',
                            'updated_at', 'checksum', 'filename',)

    def create(self, validated_data):
        attachment = AttachmentProposal.objects.create(**validated_data)
        return attachment

    def get_file(self, obj):
        """
        Trata a URL do documento
        """
        request = self.context.get('request')
        is_secure = request._request.is_secure()
        host = request._request.get_host()
        if is_secure:
            return "https://{url}{path}".format(url=host, path=obj.file.url)
        else:
            return "http://{url}{path}".format(url=host, path=obj.file.url)

    def get_filename(self, obj):
        filename = obj.file.name.split('/')[-1]
        return re.sub('\_', ' ', filename)


class ProposalSerializer(serializers.ModelSerializer):
    attachments = ProposalUploadSerializer(many=True, read_only=True)
    status = serializers.CharField()
    status_display = serializers.CharField(read_only=True)
    author = serializers.SerializerMethodField()
    class Meta:
        model = Proposal
        fields = ('user', 'author', 'title', 'number', 'status', 'created_at',
                  'attachments', 'status_display',)
        read_only_fields = ('number', 'created_at', 'attachments',
                            'status_display',)

    def get_author(self, obj):
        return obj.user.name
