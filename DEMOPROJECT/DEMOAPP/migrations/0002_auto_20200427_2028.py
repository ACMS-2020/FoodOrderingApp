# Generated by Django 2.2.12 on 2020-04-27 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 20, 28, 4, 53220)),
        ),
    ]
