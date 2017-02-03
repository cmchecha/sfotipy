# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover', models.ImageField(upload_to='images/albums/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Artist')),
            ],
        ),
    ]
