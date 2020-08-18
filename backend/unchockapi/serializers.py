from rest_framework import serializers
from rest_framework.fields import CharField

from .models import CheckIn


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'
        extra_kwargs = {
            'airline': {'required': False},
            'check_in_time': {'required': False},
            'departure_flight_time': {'required': False},
            'departure_date': {'required': False}
        }


class RequestSerializer(serializers.Serializer):
    passenger_first_name = CharField(max_length=50)
    passenger_last_name = CharField(max_length=50)
    booking_ref_num = CharField(max_length=10)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
