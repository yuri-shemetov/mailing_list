import logging

from django.core.mail import send_mail
from django.template.loader import get_template

from proj_settings.celery import app
from proj_settings.settings import EMAIL_HOST_USER


@app.task
def send_promotions_offers_mail(subject, recipient_list, template_name, context=None):
    '''
    Promotional offers
    '''
    try:
        send_mail(
            subject=subject, message=None, from_email=EMAIL_HOST_USER, recipient_list=recipient_list,
            html_message=get_template(template_name=template_name).render(context)
        )
        logging.debug("Promotion. Success!")
    except Exception as e:
        logging.info(e)


@app.task
def send_birthday_mail(subject, recipient_list, template_name, context=None):
    try:
        send_mail(
            subject=subject, message=None, from_email=EMAIL_HOST_USER, recipient_list=recipient_list,
            html_message=get_template(template_name=template_name).render(context)
        )
    except Exception as e:
        logging.info(e)
