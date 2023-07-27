from __future__ import unicode_literals

from django.forms import ModelForm

from mails.models import Mailing


class MailingForm(ModelForm):

    class Meta:
        model = Mailing
        fields = "__all__"
