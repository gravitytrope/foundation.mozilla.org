# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-19 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20170905_0026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepagehighlights',
            options={'ordering': ('_order',), 'verbose_name': 'featured highlight', 'verbose_name_plural': 'get involved (Highlights)'},
        ),
        migrations.AlterModelOptions(
            name='homepageleaders',
            options={'ordering': ('_order',), 'verbose_name': 'featured network leader', 'verbose_name_plural': 'network leaders (People)'},
        ),
        migrations.AlterModelOptions(
            name='homepagenews',
            options={'ordering': ('_order',), 'verbose_name': 'featured news item', 'verbose_name_plural': 'latest from the network (News)'},
        ),
    ]