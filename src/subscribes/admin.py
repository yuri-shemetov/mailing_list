# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from subscribes.models import Subscriber


@admin.register(Subscriber)
class SubscriberModelAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
