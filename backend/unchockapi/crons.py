from datetime import datetime
from .models import CheckIn
import logging
from django_cron import CronJobBase, Schedule

from .utils import check_into_flights

logger = logging.getLogger(__name__)


class CheckInJob(CronJobBase):
    schedule = Schedule(run_every_mins=1)
    code = 'unchockapi.check_in'

    def do(self):
        logger.error('in the def')
        check_ins = CheckIn.objects.all().filter(status__exact="FOUND").filter(check_in_time__lte=datetime.now())
        check_into_flights(check_ins)
