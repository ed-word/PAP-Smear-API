# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='svm_model',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='svm_model',
            old_name='fl_nonveg',
            new_name='Nonveg',
        ),
        migrations.RenameField(
            model_name='svm_model',
            old_name='fl_smoking',
            new_name='Smoking',
        ),
    ]
