from django.db import models
from django.utils import timezone

# Create your models here.
class TestFlow():
    def crawler():
        print('ppcwiz crawler starts..')
        # retrieve user something like this
        active_users = Info.objects.filter(user_status = 'A')
        # do the crawling job
        
    def analyzer():
        print('ppcwiz 2.0 analyzer starts..')
        # retrieve available list for anlaysis and analyze

    def submitter():
        print('ppcwiz 2.0 submitter starts..')
        # retrieve available list for submitter and submit


# sample test model
class Info(models.Model):
    USER_ACTIVE = 'A'
    USER_INACTIVE = 'I'

    USER_STATUS = [
        (USER_ACTIVE, 'ACTIVE'),
        (USER_INACTIVE, 'INACTIVE')
    ]

    user_status = models.CharField(
        max_length=1,
        default=USER_ACTIVE,
        choices=USER_STATUS
    )
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=50, null=True)
    bank_type = models.CharField(max_length=30, null=True)
    account_number = models.CharField(max_length=70, null=True)
    age = models.IntegerField(null=True)
    reg_at = models.DateField(default=timezone.now)