# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-11 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doubletap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doubletap.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doubletap.Profile')),
            ],
        ),
    ]