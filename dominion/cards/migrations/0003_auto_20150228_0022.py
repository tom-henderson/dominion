# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20150221_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['card_set', 'name']},
        ),
        migrations.AlterModelOptions(
            name='cardset',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='cardtype',
            options={'ordering': ['name']},
        ),
    ]
