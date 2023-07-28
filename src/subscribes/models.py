# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


class Subscriber(models.Model):
    SUBSCRIBER_STATUSES = [
        ("ON", "Активен"),
        ("OFF", "Нективен"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(
        max_length=512,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=512,
        verbose_name="Фамилия"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name="День рождения"
    )
    status = models.CharField(
        max_length=5,
        default="ON",
        choices=SUBSCRIBER_STATUSES,
        verbose_name="Статус"
    )

    def __str__(self):
        return self.first_name + " " + self.last_name + " / Birthday: " + str(self.birthday)

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
        indexes = [
            models.Index(fields=["email"]),
        ]
