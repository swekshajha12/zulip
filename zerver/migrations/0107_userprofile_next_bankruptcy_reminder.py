# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0106_subscription_push_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='next_bankruptcy_reminder',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
