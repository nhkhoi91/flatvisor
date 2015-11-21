# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='period',
            field=models.CharField(default=b'3 month', max_length=10, choices=[(b'3 month', b'3 months'), (b'6 month', b'6 months'), (b'9 month', b'9 months'), (b'12 month', b'12 months')]),
        ),
    ]
