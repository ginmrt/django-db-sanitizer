# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 23:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('initials', models.CharField(blank=True, default='', max_length=4)),
                ('phone', models.CharField(default='911', max_length=100)),
                ('mobile_phone', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(blank=True, default='', max_length=500)),
                ('city', models.CharField(blank=True, default='', max_length=250)),
                ('zip_code', models.CharField(blank=True, default='', max_length=25)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('awesomeness_rank', models.BigIntegerField(blank=True, default=0)),
                ('importance_rank', models.IntegerField(blank=True, default=0)),
                ('number_of_cars', models.PositiveIntegerField(blank=True, default=0)),
                ('number_of_computers', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('month_of_birth', models.CharField(blank=True, choices=[('', 'Month'), ('jan', 'January'), ('feb', 'February'), ('mar', 'March'), ('apr', 'April'), ('may', 'May'), ('jun', 'June'), ('jul', 'July'), ('aug', 'August'), ('sep', 'September'), ('oct', 'October'), ('nov', 'November'), ('dec', 'December')], max_length=3, null=True)),
                ('day_of_birth', models.IntegerField(blank=True, choices=[(None, 'Day'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], null=True)),
                ('year_of_birth', models.SmallIntegerField(blank=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('money_balance', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('internal_notes', models.TextField(blank=True, default='')),
                ('admin_notes', models.TextField(blank=True, default='', max_length=500)),
                ('is_subscribed_to_mailing', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
