import json
import logging
import random

from datetime import date
from django_celery_beat.models import PeriodicTask, CrontabSchedule

from mails.models import Mailing
from mails.tasks import send_promotions_offers_mail


def sending_router(template, subscribers, send_date=None):
    if template.mail_type == 1 and subscribers:
        for subscriber in subscribers:
            age = date.today().year - subscriber.birthday.year
            context = {
                "first_name": subscriber.first_name,
                "last_name": subscriber.last_name,
                "age": age
            }
            schedule, _ = CrontabSchedule.objects.get_or_create(
                minute="*",
                hour="*",
                day_of_week="*",
                day_of_month=subscriber.birthday.day,
                month_of_year=subscriber.birthday.month,
            )
            PeriodicTask.objects.create(
                crontab=schedule,
                name="Mailing: Birthday, " + template.title + "-" + str(subscriber.birthday) + "/" + str(random.randrange(1000)),
                task="mails.tasks.send_birthday_mail",
                args=json.dumps([template.title, [subscriber.email], template.template_path, context]),
            )
            logging.debug(subscriber.email + " Birthday. Successfully sent!")
        Mailing.active.create(
            template=template,
            subscribers=subscribers,
            send_date=subscribers[0].birthday,
            status="SENT"
        )
            
    elif template.mail_type == 2:
        if send_date:
            for subscriber in subscribers:
                schedule, _ = CrontabSchedule.objects.get_or_create(
                        minute=send_date.minute,
                        hour=send_date.hour,
                        day_of_week="*",
                        day_of_month=send_date.day,
                        month_of_year=send_date.month,
                    )
                PeriodicTask.objects.create(
                    crontab=schedule,
                    name="Mailing: Offer, " + template.title + "-" + str(send_date) + "/" + str(random.randrange(1000)),
                    task="mails.tasks.send_promotions_offers_mail",
                    args=json.dumps([template.title, [subscriber.email], template.template_path]),
                )
                logging.debug(subscriber.email + " For Send date. Offers. Successfully sent!")
            Mailing.active.create(
                template=template,
                subscribers=subscribers,
                send_date=send_date,
                status="SENT"
            )
        else:
            for subscriber in subscribers:
                send_promotions_offers_mail(
                    subject=template.title,
                    recipient_list=[subscriber.email],
                    template_name=template.template_path,
                    context=None
                )
                logging.debug(subscriber.email + " Promotions Offers. Successfully sent!")
            Mailing.active.create(
                template=template,
                subscribers=subscribers,
                send_date=send_date,
                status="SENT"
            )
    else:
        logging.debug("Didn't choose a mailing type!")
