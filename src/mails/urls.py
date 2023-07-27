from __future__ import unicode_literals

from django.conf.urls import url

from mails.views import CreateMailingView

urlpatterns = [
    url(r'^create/', CreateMailingView.as_view(), name="create_mailing"),
]
