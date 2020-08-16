from .exceptions import ConflictException
from .serializers import CheckInSerializer, ResponseSerializer, RequestSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_flight_info_and_create_check_ins


# Create your views here.
class CheckInView(APIView):
    """
    Enter in the information to check into your flight
    """

    def post(self, request, format=None):
        request_serializer = RequestSerializer(data=request.data)

        if request_serializer.is_valid():
            try:
                check_in_response = get_flight_info_and_create_check_ins(request_serializer.validated_data)
                response_serializer = ResponseSerializer(check_in_response)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            except ConflictException as exception:
                return Response(data=exception.message, status=exception.status)
        return Response(request_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
