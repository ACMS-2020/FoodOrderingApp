# Generated by Django 3.0.5 on 2020-04-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditems', '0002_auto_20200426_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='num_customers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
