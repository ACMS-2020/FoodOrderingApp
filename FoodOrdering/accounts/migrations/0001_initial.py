# Generated by Django 3.0.5 on 2020-05-14 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('type1', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('Location', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAgent',
            fields=[
                ('username', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('rating', models.CharField(default='', max_length=20)),
                ('vehicleNumber', models.CharField(default='', max_length=10)),
                ('status', models.BooleanField(default=False)),
                ('drivingLicense', models.CharField(default='', max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('username', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('name', models.CharField(default='', max_length=20)),
                ('Location', models.CharField(default='', max_length=100)),
                ('startTime', models.TimeField(default='00:00')),
                ('closeTime', models.TimeField(default='00:00')),
                ('cuisine', models.CharField(default='', max_length=20)),
                ('pricePerHead', models.IntegerField(default=0)),
                ('contactNumber', models.CharField(default='', max_length=10)),
                ('review', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
