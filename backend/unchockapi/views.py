from django.views.decorators.csrf import csrf_exempt

from .models import CheckIn
from .serializers import CheckInSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CheckInView(APIView):
    """
    Enter in the information to check into your flight
    """
    def post(self, request, format=None):
        # Get the request data,
        # check_in = request.data
        # flights, passengers = get_flight_info_and_create_check_ins(new_check_in['booking_ref_num'],
        #                                                            new_check_in['passenger_first_name'],
        #                                                            new_check_in['passenger_last_name'], airline)

        return Response({}, status=status.HTTP_201_CREATED)
