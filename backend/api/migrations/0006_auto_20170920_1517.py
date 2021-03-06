# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_projectmembership_club'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='clubs',
            new_name='collaborating_clubs',
        ),
        migrations.AddField(
            model_name='project',
            name='owner_club',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='api.Club'),
            preserve_default=False,
        ),
    ]
