from __future__ import unicode_literals

from django.forms import (
    DateInput, ModelForm, Select, SelectMultiple
)

from datetime import date

from mails.models import Mailing


class MailingForm(ModelForm):

    class Meta:
        model = Mailing
        fields = ('template', 'subscribers', 'send_date')
        labels = {
            'template': 'Please choose a template',
            'subscribers': 'Subscribers',
            'send_date': 'Date for send',
        }
        widgets = {
            'template': Select(attrs={
                'class': 'form-select'
            }),
            'subscribers': SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'send_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemple: ' + str(date.today()) + ' 17:00 (may be empty)'
            }),
        }
 