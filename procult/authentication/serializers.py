# -*- coding: utf-8 -*-

from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=False)
    password2 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'cpf', 'cnpj', 'ceac',
                  'password1', 'password2', 'is_admin',)
        read_only_fields = ('created_at', 'updated_at', 'is_admin')

    def create(self, validated_data):
        password1 = validated_data.pop('password1', None)
        password2 = validated_data.pop('password2', None)

        if password1 and password2 and password1 == password2:
            user = User.objects.create(**validated_data)
            user.set_password(password1)
            user.save()
        else:
            raise serializers.ValidationError(
                {'password2', 'As senhas não se batem. Digite novamente'}
            )

        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.cnpj = validated_data.get('cnpj', instance.cnpj)
        instance.ceac = validated_data.get('ceac', instance.ceac)

        instance.save()

        password = validated_data.get('password1', None)
        confirm_password = validated_data.get('password2', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)

        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
