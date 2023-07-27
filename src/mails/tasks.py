import logging

from django.core.mail import send_mail
from django.template.loader import get_template

from proj_settings.celery import app


@app.task
def send_promotions_offers_mail(subject, recipient_list, template_name, context):
    '''
    Promotional offers
    '''
    try:
        send_mail(
            subject=subject, message=None, from_email=None, recipient_list=recipient_list, fail_silently=True,
            html_message=get_template(template_name=template_name).render(context)
        )
    except Exception as e:
        logging.info(e)


@app.task
def send_birthday_mail(subject, recipient_list, template_name, context):
    try:
        send_mail(
            subject=subject, message=None, from_email=None, recipient_list=recipient_list, fail_silently=True,
            html_message=get_template(template_name=template_name).render(context)
        )
    except Exception as e:
        logging.info(e)