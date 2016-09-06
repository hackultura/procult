# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from procult.authentication.views import (
    UserViewSet,
    ProposalViewSet,
    LoginView,
    ChangePasswordView,
    ProposalView,
    ProposalUploadFilesView,
    ProposalUploadFilesDetailView,
    ProposalDetailView,
    ProposalDashboardView,
    ProposalNoticeDashboardView,
    ProposalAnalisysDetailView,
    ExportProposalsView,
    CompressProposalFilesView,
    ProposalOwnListView,
    ProposalOwnByNoticeListView,
    ProposalNoticeView,
    NoticeView,
    NoticeDetailView
)

admin.autodiscover()

router = DefaultRouter()

router.register(r'api/v1/usuarios', UserViewSet)
urlpatterns = router.urls

urlpatterns += [
    url(r'^api/v1/auth/login/$', LoginView.as_view()),
    url(r'^api/v1/auth/password/change/(?P<user_pk>\d+)/$',
        ChangePasswordView.as_view()),
    url(r'^api/v1/propostas/$', ProposalView.as_view()),
    url(r'^api/v1/propostas/export/csv/$', ExportProposalsView.as_view()),
    url(r'^api/v1/propostas/(?P<number>\d+)/$',
        ProposalDetailView.as_view()),
    url(r'^api/v1/propostas/(?P<number>\d+)/upload/$',
        ProposalUploadFilesView.as_view()),
    url(r'^api/v1/propostas/(?P<number>\d+)/zip/$',
        CompressProposalFilesView.as_view()),
    url(r'^api/v1/propostas/documentos/(?P<uid>[a-zA-Z0-9\-]+)/$',
        ProposalUploadFilesDetailView.as_view()),
    url(r'^api/v1/propostas/user/(?P<user_pk>\d+)/$',
        ProposalOwnListView.as_view()),
    url(r'^api/v1/propostas/user/(?P<user_pk>\d+)/(?P<notice_pk>\d+)/$',
        ProposalOwnByNoticeListView.as_view()),
    url(r'^api/v1/propostas/dashboard/$', ProposalDashboardView.as_view()),
    url(r'^api/v1/propostas/dashboard/(?P<notice_id>\d+)/$', ProposalNoticeDashboardView.as_view()),
    url(r'^api/v1/editais/(?P<notice>\d+)/$',
        ProposalNoticeView.as_view()),


    url(r'^api/v1/editais/$', NoticeView.as_view()),
    url(r'^api/v1/edital/(?P<id>\d+)/$',
        NoticeDetailView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
