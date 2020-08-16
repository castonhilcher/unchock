class CheckInResponse:
    def __init__(self):
        self.flights = []

    def add_check_in(self, check_in):
        self.flights.append(check_in)
