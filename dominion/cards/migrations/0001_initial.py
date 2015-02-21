# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('cost_gold', models.IntegerField()),
                ('cost_potions', models.IntegerField()),
                ('rules', models.CharField(max_length=350)),
                ('image_url', models.CharField(max_length=100)),
                ('image', models.ImageField(height_field=b'image_height', width_field=b'image_width', null=True, upload_to=b'cards/', blank=True)),
                ('image_height', models.IntegerField(null=True, blank=True)),
                ('image_width', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='card_set',
            field=models.ForeignKey(to='cards.CardSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.ForeignKey(to='cards.CardType'),
            preserve_default=True,
        ),
    ]
