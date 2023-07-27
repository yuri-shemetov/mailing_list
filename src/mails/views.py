# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

from mails.forms import MailingForm
from mails.services import sending_router


class CreateMailingView(View):
    def get(self, request):
        return render(request, "mails/create.html", {"form": MailingForm()})

    def post(self, request):
        form = MailingForm(request.POST or None)
        if form.is_valid():
            sending_router(
                template=form.cleaned_data.get("template"),
                subscribers=form.cleaned_data.get("subscribers"),
                send_date=form.cleaned_data.get("send_date") or None
            )

            return render(request, "mails/success.html")
        else:
            return render(request, "mails/create.html", {"form": MailingForm()})
