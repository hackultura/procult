# -*- coding: utf-8 -*-

import re
import bitmath
import os

from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from django.utils import timezone
from rest_framework import serializers
from .models import Proposal, AttachmentProposal, Notice, ProposalTag


class ProposalUploadSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(format='hex', required=False)
    file = serializers.FileField(max_length=255, write_only=True)
    file = serializers.SerializerMethodField()
    filename = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    class Meta:
        model = AttachmentProposal
        fields = ('file', 'uid', 'checksum', 'filename', 'size',)
        read_only_fields = ('uuid', 'file', 'created_at', 'size',
                            'updated_at', 'checksum', 'filename',)

    def _validate_file(self, file):
        if file in [None, '']:
            raise serializers.ValidationError("Ocorreu um erro no upload. Tente novamente")
        elif file.content_type not in settings.ALLOWED_FILES:
            raise serializers.ValidationError("Formato de arquivo inválido para o projeto.")
        return True

    def create(self, validated_data):
        if self._validate_file(validated_data.get('file')):
            attachment = AttachmentProposal.objects.create(**validated_data)
        return attachment

    def get_file(self, obj):
        """
        Trata a URL do documento
        """
        if not obj.file:
            return "Not a valid file."

        request = self.context.get('request')
        is_secure = request._request.is_secure()
        host = request._request.get_host()
        if is_secure:
            return "https://{url}{path}".format(url=host, path=obj.file.url)
        else:
            return "http://{url}{path}".format(url=host, path=obj.file.url)

    def get_filename(self, obj):
        if not obj.file or not os.path.isfile(obj.file.path):
            return "File not found on server."

        filename = obj.file.name.split('/')[-1]
        return re.sub('\_', ' ', filename)

    def get_size(self, obj):
        if not obj.file or not os.path.isfile(obj.file.path):
            return "File not found on server."

        return bitmath.Byte(obj.file.size).best_prefix().format(
            "{value:.2f} {unit}")


class ProposalSerializer(serializers.ModelSerializer):
    attachments = ProposalUploadSerializer(many=True, read_only=True)
    status = serializers.CharField()
    status_display = serializers.CharField(read_only=True)
    tag_name = serializers.CharField(read_only=True)
    ente_info = serializers.SerializerMethodField()

    class Meta:
        model = Proposal
        fields = ('ente', 'ente_info', 'title', 'id', 'number', 'status', 'created_at',
                  'attachments', 'status_display', 'sended_at', 'notice', 'tag', 'tag_name')
        read_only_fields = ('number', 'created_at', 'attachments',
                            'status_display', 'ente_detail', 'tag_name')

    def validate_ente(self, value):
        if not value.cpf and not value.cnpj:
            raise serializers.ValidationError(
                "Não pode criar propostas com um usuário sem CPF ou CNPJ."
            )
        return value

    def validate_status(self, value):
        if value == Proposal.STATUS_CHOICES.sended:
            self.initial_data['sended_at'] = timezone.now()

        return value

    def validate(self, data):
        if not data['notice']:
            raise serializers.ValidationError(
                {"missing": "Edital não associado."}
                )

        is_available = data['notice'].is_available

        if is_available is False:
            raise serializers.ValidationError(
                {"availability": "Envio de propostas encerrado."}
            )

        return data

    def get_ente_info(self, obj):
        ente = {
            'author': obj.ente.user.name,
            'ceac': obj.ente.ceac
        }
        if obj.ente.cpf not in [None, '']:
            ente['cpf'] = obj.ente.cpf
        else:
            ente['cnpj'] = obj.ente.cnpj
        return ente


class ProposalLastSendedSerializer(serializers.ModelSerializer):
    ente_info = serializers.SerializerMethodField()
    class Meta:
        model = Proposal
        fields = ('ente_info', 'title', 'id', 'number', 'status', 'notice',
                  'status_display',)

    def get_ente_info(self, obj):
        ente = {
            'author': obj.ente.user.name,
            'ceac': obj.ente.ceac
        }
        if obj.ente.cpf not in [None, '']:
            ente['cpf'] = obj.ente.cpf
        else:
            ente['cnpj'] = obj.ente.cnpj
        return ente


class ProposalLastAnalyzedSerializer(serializers.ModelSerializer):
    ente_info = serializers.SerializerMethodField()
    class Meta:
        model = Proposal
        queryset = Proposal.objects.last_analyzed()
        fields = ('ente_info', 'title', 'id', 'number', 'status', 'notice',
                  'status_display')

    def get_ente_info(self, obj):
        ente = {
            'author': obj.ente.user.name,
            'ceac': obj.ente.ceac
        }
        if obj.ente.cpf not in [None, '']:
            ente['cpf'] = obj.ente.cpf
        else:
            ente['cnpj'] = obj.ente.cnpj
        return ente


class NoticeSerializerCreate(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    is_available = serializers.BooleanField()

    class Meta:
        model = Notice
        fields = ('id', 'title', 'description', 'is_available', 'tags_available')
        read_only_fields = ('id', 'tags_available')


class NoticeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    is_available = serializers.BooleanField()

    class Meta:
        model = Notice
        fields = ('id', 'title', 'description', 'is_available', 'tags_available')
        read_only_fields = ('id',)


class ProposalTagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = ProposalTag
        fields = ('id', 'name')


class NoticeNameIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('title', 'id')
        read_only_fields = ('title', 'id')


class TagNameIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProposalTag
        fields = ('name', 'id')
        read_only_fields = ('name', 'id')