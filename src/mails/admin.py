# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mails.models import Mailing, MailTemplate


@admin.register(MailTemplate)
class MailTemplateModelAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Mailing)
class MailingModelAdmin(admin.ModelAdmin):
    list_display = ("template", "status")
