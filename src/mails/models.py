# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid

from subscribes.models import Subscriber


class MailTemplate(models.Model):

    MAIL_TYPES = [
        (1, "Birthday"),
        (2, "Offers"),
    ]

    TEMPLATE_STATUSES = [
        ("ON", "Активен"),
        ("OFF", "В архиве"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        max_length=512,
        verbose_name="Наименование шаблона"
    )
    template_path = models.TextField( 
        help_text="Example:'mails/birthday.html'",
        verbose_name="Путь к шаблону"
    )
    mail_type = models.IntegerField(
        choices=MAIL_TYPES,
        default=1,
        verbose_name="Тип"
    )
    status = models.CharField(
        max_length=10,
        default="ON",
        choices=TEMPLATE_STATUSES,
        verbose_name="Статус")

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
        ("CREATED", "Создано"),
        ("SENT", "Отправлено"),
        ("RECEIVED", "Получено"),
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
        null=True, 
        blank=True
    )
    status = models.CharField(
        max_length=10, 
        default="CREATED",
        choices=MAILING_STATUSES,
        verbose_name="Статус"
    )
    active = models.Manager()

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
