from django import forms
from django.core.exceptions import ValidationError

from .serializers import EnteSerializer
from .models import Ente


class EnteForm(forms.ModelForm):

    def serializer_validate(self, fieldname):
        ente_serializer = EnteSerializer(data=self.cleaned_data)

        if ente_serializer.is_valid() is False:
            if ente_serializer.errors.get(fieldname, None):
                print ente_serializer.errors
                raise ValidationError(ente_serializer.errors[fieldname])

        return self.cleaned_data[fieldname]

    def clean_cpf(self):
        return self.serializer_validate('cpf')

    def clean_cnpj(self):
        return self.serializer_validate('cnpj')

    def clean_ceac(self):
        return self.serializer_validate('ceac')

    class Meta:
        model = Ente
        fields = ['user', 'cpf', 'cnpj', 'ceac']
