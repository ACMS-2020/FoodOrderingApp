# Generated by Django 3.0.5 on 2020-04-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('email_id', models.CharField(max_length=30)),
            ],
        ),
    ]