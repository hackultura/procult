# -*- coding: utf-8 -*-

from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from procult.authentication.views import (
    UserViewSet,
    LoginView,
    ChangePasswordView,
    ProposalView,
    ProposalUploadFilesView,
    ProposalUploadFilesDetailView,
    ProposalDetailView,
    ProposalDashboardView,
    ExportProposalsView,
    CompressProposalFilesView,
    ProposalOwnListView
)

router = DefaultRouter()

router.register(r'usuarios', UserViewSet)
urlpatterns = router.urls

urlpatterns += [
    url(r'^auth/login/$', LoginView.as_view()),
    url(r'^auth/password/change/(?P<user_pk>\d+)/$',
        ChangePasswordView.as_view()),
    url(r'^propostas/$', ProposalView.as_view()),
    url(r'^propostas/export/csv/$', ExportProposalsView.as_view()),
    url(r'^propostas/(?P<number>\d+)/$',
        ProposalDetailView.as_view()),
    url(r'^propostas/(?P<number>\d+)/upload/$',
        ProposalUploadFilesView.as_view()),
    url(r'^propostas/(?P<number>\d+)/zip/$',
        CompressProposalFilesView.as_view()),
    url(r'^propostas/documentos/(?P<uid>[a-zA-Z0-9\-]+)/$',
        ProposalUploadFilesDetailView.as_view()),
    url(r'^propostas/user/(?P<user_pk>\d+)/$',
        ProposalOwnListView.as_view()),
    url(r'^propostas/dashboard/$', ProposalDashboardView.as_view()),
]
