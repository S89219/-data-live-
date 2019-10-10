# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-18 07:25


from __future__ import absolute_import, print_function, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0008_auto_20181014_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='origin',
            field=models.CharField(help_text="The origin of the address: the user's email address, or 'author: DRAFTNAME' if a draft, or 'role: GROUP/ROLE' if a role.", max_length=150),
        ),
        migrations.AlterField(
            model_name='historicalemail',
            name='origin',
            field=models.CharField(help_text="The origin of the address: the user's email address, or 'author: DRAFTNAME' if a draft, or 'role: GROUP/ROLE' if a role.", max_length=150),
        ),
    ]