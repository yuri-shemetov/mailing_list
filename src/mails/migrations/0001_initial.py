# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-07-26 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscribes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CREATED', '\u0421\u043e\u0437\u0434\u0430\u043d\u0430'), ('SENT', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430'), ('RECEIVED', '\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0430')], default='CREATED', max_length=10, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0441\u0441\u044b\u043b\u043a\u0430',
                'verbose_name_plural': '\u0420\u0430\u0441\u0441\u044b\u043b\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='MailTemplate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=512, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u0430')),
            ],
            options={
                'verbose_name': '\u0428\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u043f\u0438\u0441\u044c\u043c\u0430',
                'verbose_name_plural': '\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u0434\u043b\u044f \u043f\u0438\u0441\u0435\u043c',
            },
        ),
        migrations.AddIndex(
            model_name='mailtemplate',
            index=models.Index(fields=['title'], name='mails_mailt_title_cc1c47_idx'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='subscribers',
            field=models.ManyToManyField(to='subscribes.Subscriber', verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailings', to='mails.MailTemplate', verbose_name='\u0428\u0430\u0431\u043b\u043e\u043d'),
        ),
    ]
