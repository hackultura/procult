# -*- coding: utf-8 -*-

from django.conf.urls import url

from procult.notice.views import CategoryView, CategoryDetailView

urlpatterns = [
    url(r'^categorias/(?P<uid>[a-zA-Z0-9\-]+)$', CategoryDetailView.as_view()),
    url(r'^categorias/', CategoryView.as_view()),
]
