import json
import logging

from datetime import datetime
from django_celery_beat.models import PeriodicTask, CrontabSchedule

from mails.models import Mailing
from mails.tasks import send_promotions_offers_mail


def sending_router(template, subscribers, send_date=None):
    if template.mail_type == 0:
        if len(subscribers) == 1:
            subscriber = subscribers[0]
            age = datetime.now() - subscriber.birthday
            context = {
                "first_name": subscriber.first_name,
                "last_name": subscriber.last_name,
                "age": age.year
            }
            PeriodicTask.objects.create(
                crontab=CrontabSchedule.objects.get_or_create(
                    minute="30",
                    hour="9",
                    day_of_week="*",
                    day_of_month=subscriber.birthday.day,
                    month_of_year=subscriber.birthday.month,
                ),
                name="Mailing: Birthday, " + template.title + "-" + subscriber.birthday,
                task="mailing.tasks.send_birthday_mail",
                args=json.dumps([template.title, [subscriber.email], template.template_path, context]),
            )
            Mailing.active.create(
                template=template,
                subscribers=subscribers,
                send_date=subscriber.birthday,
                status="SENT"
            )
        else:
            logging.info("Bad Request. The subscriber must been only 1.")
    elif template.mail_type == 1:
        if send_date:
            for subscriber in subscribers:
                PeriodicTask.objects.create(
                    crontab=CrontabSchedule.objects.get_or_create(
                        minute=send_date.minute,
                        hour=send_date.hour,
                        day_of_week="*",
                        day_of_month=send_date.day,
                        month_of_year=send_date.month,
                    ),
                    name="Mailing: Offer, " + template.title + "-" + send_date,
                    task="mailing.tasks.send_promotions_offers_mail",
                    args=json.dumps([template.title, [subscriber.email], template.template_path]),
                )
            Mailing.active.create(
                template=template,
                subscribers=subscribers,
                send_date=send_date,
                status="SENT"
            )
        else:
            for subscriber in subscribers:
                send_promotions_offers_mail.delay(
                    subject=template.title,
                    recipient_list=[subscriber.email],
                    template_name=template.template_path,
                )
            Mailing.active.create(
                template=template,
                subscribers=subscribers,
                send_date=send_date,
                status="SENT"
            )
