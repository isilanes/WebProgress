# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pesos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeInstant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0.0, verbose_name='Weight')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pesos.Person')),
                ('when', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pesos.TimeInstant')),
            ],
        ),
    ]