# Generated by Django 3.1 on 2020-08-28 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unchockapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='from_city',
            field=models.CharField(default='HEY', max_length=50, verbose_name='Last name of the passenger to check in'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkin',
            name='to_city',
            field=models.CharField(default='HEY', max_length=50, verbose_name='Last name of the passenger to check in'),
            preserve_default=False,
        ),
    ]
