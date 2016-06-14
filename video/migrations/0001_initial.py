# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=128)),
                ('site_code', models.CharField(max_length=128)),
                ('site_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='belong_site',
            field=models.ForeignKey(to='video.site'),
        ),
    ]
