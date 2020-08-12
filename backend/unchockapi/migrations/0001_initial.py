# Generated by Django 2.1.4 on 2020-08-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=30, verbose_name='Name of Airline')),
                ('booking_ref_num', models.CharField(max_length=10, verbose_name='Booking reference number')),
                ('passenger_first_name', models.CharField(max_length=50, verbose_name='First name of the passenger to check in')),
                ('passenger_last_name', models.CharField(max_length=50, verbose_name='Last name of the passenger to check in')),
                ('check_in_time', models.DateTimeField(verbose_name='Date and time check in is allowed')),
                ('departure_flight_time', models.DateTimeField(verbose_name='Date and time the flight will take off')),
                ('departure_date', models.DateField(verbose_name='Date and time the flight will take off')),
                ('status', models.CharField(default='READY', max_length=10, verbose_name='Status of the check-in')),
                ('create_ts', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time the check in was created')),
                ('update_ts', models.DateTimeField(auto_now=True, verbose_name='Date and Time the check in information was updated')),
            ],
            options={
                'db_table': 'check_in',
            },
        ),
    ]