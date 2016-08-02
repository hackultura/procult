# -*- coding: utf-8 -*-

from rest_framework import generics

from procult.notice.serializers import CategorySerializer
from procult.notice.models import Category


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.root_nodes()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.root_nodes()
    lookup_field = 'uid'
    serializer_class = CategorySerializer
