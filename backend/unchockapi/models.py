from django.db import models


class CheckIn(models.Model):
    class Meta:
        db_table = 'check_in'
        unique_together = ('booking_ref_num', 'passenger_first_name', 'passenger_last_name', 'departure_date')

    booking_ref_num = models.CharField('Booking reference number', max_length=10, null=False)
    passenger_first_name = models.CharField('First name of the passenger to check in', max_length=50, null=False)
    passenger_last_name = models.CharField('Last name of the passenger to check in', max_length=50, null=False)
    check_in_time = models.DateTimeField('Date and time check in is allowed', null=False)
    departure_flight_time = models.DateTimeField('Date and time the flight will take off', null=False)
    departure_date = models.DateField('Date and time the flight will take off', null=False)
    status = models.CharField('Status of the check-in', max_length=10, null=False, default='READY')
    create_ts = models.DateTimeField('Date and Time the check in was created', auto_now_add=True, null=False)
    update_ts = models.DateTimeField('Date and Time the check in information was updated', null=False, auto_now=True)

    def __str__(self):
        return self.passenger_first_name + ' ' + self.passenger_last_name + ' - ' + self.booking_ref_num
