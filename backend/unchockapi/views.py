from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
from background_task import background

from .exceptions import ConflictException
from .models import CheckIn
from .serializers import CheckInSerializer, RequestSerializer
from .utils import get_flight_info_and_create_check_ins, check_into_flights


# Create your views here.
class CheckInView(APIView):
    """
    Enter in the information to check into your flight
    """
    def post(self, request, format=None):
        request_serializer = RequestSerializer(data=request.data)

        if request_serializer.is_valid():
            try:
                check_ins = get_flight_info_and_create_check_ins(request_serializer.validated_data)
                for check_in in check_ins:
                    check_in_to_flights_job(check_in.id, schedule=check_in.check_in_time)
                serializer = CheckInSerializer(check_ins, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ConflictException as exception:
                return Response(data=exception.message, status=exception.status)
        return Response(request_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    """
        Gets all the current flights
    """
    def get(self, request, format=None):

        serializer = CheckInSerializer(CheckIn.objects.all(), many=True)
        return Response(serializer.data)


@background(schedule=60)
def check_in_to_flights_job(pk):
    # lookup user by id and send them a message
    check_in = CheckIn.objects.get(pk=pk)

    check_into_flights(check_in)
