from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from .models import CheckIn


def check_in():
    check_ins = CheckIn.objects.all().filter(status__exact="FOUND").filter(check_in_time__lte=datetime.now())
    for check_in in check_ins:
        print(check_in)
