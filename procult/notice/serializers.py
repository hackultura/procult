# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from procult.core.utils import validate_uuid
from procult.notice.models import Category


class RecursiveField(serializers.BaseSerializer):
    """
    Cria instancia do serializer parente e retorna os dados
    serializados.
    """
    def to_representation(self, value):
        ParentSerializer = self.parent.parent.__class__
        serializer = ParentSerializer(value, context=self.context)
        return serializer.data

    def to_internal_value(self, data):
        ParentSerializer = self.parent.parent.__class__
        Model = ParentSerializer.Meta.model
        try:
            if isinstance(data, str) and validate_uuid(data):
                instance = Model.objects.get(uid=data)
            if isinstance(data, dict):
                return data
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                "Objeto {0} não encontrado".format(
                    Model().__class__.__name__
                )
            )
        return instance


class CategorySerializer(serializers.ModelSerializer):
    subcategories = RecursiveField(many=True, required=False)

    class Meta:
        model = Category
        fields = ("uid", "name", "subcategories",)

    def create(self, validated_data):
        name = validated_data.pop('name')
        subcategories = validated_data.get('subcategories', [])

        category = Category.objects.create(name=name)
        for subcategory in subcategories:
            subcategory['parent'] = category
            Category.objects.get_or_create(**subcategory)

        return category

    def update(self, instance, validated_data):
        import ipdb; ipdb.set_trace()
        name = validated_data.get('name', instance.name)
        subcategories = validated_data.get('subcategories', [])

        instance.name = name
        for subcategory in subcategories:
            subinstance, created = Category.objects.get_or_create(
                **subcategory
            )
            subinstance.parent = instance
            subinstance.save()

        instance.save()
        return instance
