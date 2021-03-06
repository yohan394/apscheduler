import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from django_apscheduler.jobstores import register_events, register_job
from pytz import utc
from .models import TestFlow as testFlow
from django.conf import settings


# Create scheduler to run in a thread inside the application process
scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)

def start():
    if settings.DEBUG:
      	# Hook into the apscheduler logger
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)

        
    # Adding this job here
    # This will do the following:
    # - Add a scheduled job to the job store on application initialization
    # - replace_existing in combination with the unique ID prevents duplicate copies of the job

    # interval 
    scheduler.add_job(func = testFlow.crawler, trigger='interval', seconds=90, id="crawler", replace_existing=True)
    # executed at 12:30 am daily
    scheduler.add_job(func = testFlow.analyzer, trigger='cron', hour=0, minute=30, id="analyzer", replace_existing=True)
    # this acts like an interval
    scheduler.add_job(func = testFlow.submitter, trigger='cron', second='*/50', id="submitter", replace_existing=True)

    # Add the scheduled jobs to the Django admin interface
    # register_events(scheduler) // deprecated

    scheduler.start()