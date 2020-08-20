import requests
import json

from django.db import IntegrityError

from .classes import CheckInResponse
from .exceptions import ConflictException
from .models import CheckIn
import pendulum
import logging
from datetime import timedelta

logger = logging.getLogger(__name__)

# Host urls
SOUTHWEST_HOST = 'https://www.southwest.com'


# endpoints
SOUTHWEST_GET_FLIGHT = '/api/air-misc/v1/air-misc/page/air/manage-reservation/view'


# Southwest Response Constants
class SouthwestResponseStatus:
    def __init__(self, code, search_string):
        self.code = code
        self.search_string = search_string


# Statuses to search for in the response
RESPONSE_STATUS_SUCCESS = SouthwestResponseStatus(1, "")
RESPONSE_STATUS_TOO_EARLY = SouthwestResponseStatus(0, "DEPARTURE_DATE_IS_TOO_SOON")
RESPONSE_STATUS_INVALID = SouthwestResponseStatus(-1, "CONFIRMATION_NUMBER__DOES_NOT_MATCH")
RESPONSE_STATUS_RES_NOT_FOUND = SouthwestResponseStatus(-2, "RESERVATION_NOT_FOUND")
RESPONSE_STATUS_INVALID_PASSENGER_NAME = SouthwestResponseStatus(-3, "PASSENGER_IS_NOT_IN_RESERVATION")
RESPONSE_STATUS_RESERVATION_CANCELLED = SouthwestResponseStatus(-4, "Your reservation has been cancelled")
RESPONSE_STATUS_FLIGHT_FINALIZED = SouthwestResponseStatus(-5, "FLIGHT_FINALIZED")
RESPONSE_STATUS_UNKNOWN_FAILURE = SouthwestResponseStatus(-100, None)

# Default headers
SOUTHWEST_HEADERS = requests.utils.default_headers()
SOUTHWEST_HEADERS.update({
    "origin": "https://www.southwest.com",
    "pragma": "no-cache",
    "referer": "https://www.southwest.com/air/check-in/index.html?redirectToVision=true&leapfrogRequest=true",
    "x-channel-id": "southwest",
    "x-api-key": "l7xx944d175ea25f4b9c903a583ea82a1c4c",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "null null",
    "cache-control": "no-cache",
    "content-type": "application/json"
})


def get_flight_info_and_create_check_ins(passenger_confirmation):
    session = requests.Session()
    session.get(SOUTHWEST_HOST)
    data = {
        "confirmationNumber": passenger_confirmation['booking_ref_num'],
        "passengerFirstName": passenger_confirmation['passenger_first_name'],
        "passengerLastName": passenger_confirmation['passenger_last_name'],
        "application": "air-manage-reservation",
        "site": "southwest"
    }

    logger.error(data)
    response = session.post(SOUTHWEST_HOST + SOUTHWEST_GET_FLIGHT, data=json.dumps(data), headers=SOUTHWEST_HEADERS)
    if response.status_code != 200:
        logger.error(response.json())
        raise Exception('response status needs to be 200. actual value was {status}'.format(status=response.status_code))

    response_object = response.json()

    check_ins = []
    for reservation in response_object['data']['searchResults']['reservations']:
        for passenger in reservation['air']['ADULT']['passengers']:
            departure_date = None
            for bound in reservation['air']['bounds']:
                if departure_date != bound['departureDate']:
                    departure_date = bound['departureDate']
                    departure_date_time = pendulum.parse(bound['stopsDetails'][0]['departureDateTime'])

                    # Try to insert, if it already exists, catch the error and return custom exception
                    try:
                        check_in = CheckIn.objects.create(
                            status='FOUND',
                            passenger_last_name=passenger['name']['lastName'],
                            passenger_first_name=passenger['name']['firstName'],
                            booking_ref_num=passenger['confirmationNumber'],
                            departure_flight_time=departure_date_time,
                            departure_date=departure_date,
                            check_in_time=departure_date_time - timedelta(days=1)
                        )
                        check_ins.append(check_in)
                    except IntegrityError as error:
                        raise ConflictException("Duplicate key in the table")

    return check_ins