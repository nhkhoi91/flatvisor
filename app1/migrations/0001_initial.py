# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flat_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('free_from_date', models.DateTimeField(verbose_name=b'date free')),
                ('occupied', models.BooleanField()),
                ('period', models.CharField(default=b'3 month', max_length=2, choices=[(b'3 month', b'3 months'), (b'6 month', b'6 months'), (b'9 month', b'9 months'), (b'12 month', b'12 months')])),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='flat',
            field=models.ForeignKey(to='app1.Flat'),
        ),
    ]
