# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20151121_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='flat',
            field=models.ForeignKey(to='app1.Flat', blank=True),
        ),
    ]
