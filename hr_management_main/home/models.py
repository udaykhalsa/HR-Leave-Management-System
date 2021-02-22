from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, auth


class LeaveApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             default=1, related_name='reason', null=True, blank=True)
    reason = models.CharField(max_length=255, null=False)
    from_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False, null=False)

class LeaveList(models.Model):
    Choice = [
        ('Approved', 'Approved'),
        ('Denied', 'Denied')
    ]
    # id = models.ForeignKey(LeaveApplication, max_length=255, on_delete=models.CASCADE)
    user = models.CharField(max_length=50, null=False)
    reason = models.CharField(max_length=255, null=False)
    from_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    leave_status = models.CharField(choices=Choice, max_length=50)