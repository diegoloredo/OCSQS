# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('meta_model', models.CharField(max_length=100, choices=[(b'1', b'Model Node'), (b'2', b'Another Node')])),
                ('meta_instance', models.CharField(max_length=100)),
                ('meta_human_readable', models.CharField(max_length=100)),
            ],
        ),
    ]
