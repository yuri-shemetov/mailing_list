# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid

from subscribes.models import Subscriber


class MailTemplate(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        max_length=512,
        verbose_name="Наименование шаблона"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Шаблон для письма"
        verbose_name_plural = "Шаблоны для писем"
        indexes = [
            models.Index(fields=["title"]),
        ]


class Mailing(models.Model):
    MAILING_STATUSES = [
        ("CREATED", "Создана"),
        ("SENT", "Отправлена"),
        ("RECEIVED", "Получена"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    subscribers = models.ManyToManyField(
        Subscriber,
        verbose_name="Подписчики"
    )
    template = models.ForeignKey(
        MailTemplate,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="Шаблон"
    )

    send_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.CharField(
        max_length=10, 
        default="CREATED",
        choices=MAILING_STATUSES,
        verbose_name="Статус"
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
