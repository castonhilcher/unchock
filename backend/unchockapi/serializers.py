from rest_framework import serializers
from .models import CheckIn


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('airline', 'booking_ref_num', 'passenger_first_name', 'passenger_last_name')
