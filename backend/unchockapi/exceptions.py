from rest_framework import status


class ConflictException(Exception):
    def __init__(self, message):
        self.message = message
        self.status = status.HTTP_409_CONFLICT
        super().__init__(self.message)
