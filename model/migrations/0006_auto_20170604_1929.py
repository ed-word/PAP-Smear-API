# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_auto_20170604_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='svm_model',
            old_name='HGB',
            new_name='Haemoglobin',
        ),
        migrations.RenameField(
            model_name='svm_model',
            old_name='WBCLAB',
            new_name='WBC',
        ),
    ]
