# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import toastr.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toastr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=1000)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Toastr',
                'verbose_name_plural': 'Toastrs',
            },
        ),
        migrations.CreateModel(
            name='ToastrType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('color', models.CharField(default='ffffff', max_length=6, validators=[toastr.models.validate_hex_color])),
            ],
            options={
                'verbose_name': 'Toastr Type',
                'verbose_name_plural': 'Toastr Types',
            },
        ),
        migrations.AddField(
            model_name='toastr',
            name='toastr_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toastr.ToastrType'),
        )
    ]
