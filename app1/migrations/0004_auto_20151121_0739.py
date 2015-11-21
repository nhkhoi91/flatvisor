# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20151121_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='flat',
            field=models.ForeignKey(blank=True, to='app1.Flat', null=True),
        ),
    ]
