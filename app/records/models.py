import datetime

from django.db import models

# Create your models here.
from members.models import User


class Record(models.Model):
    SERVICE_TYPE = [
        ('Saturday Worship', 'Sunday 4 Part'),
        ('Sunday Part 1 Worship', 'Sunday 1 Part'),
        ('Sunday Part 2 Worship', 'Sunday 2 Part'),
        ('Sunday Part 3 Worship', 'Sunday 3 Part'),
        ('Sunday Part 4 Worship', 'Sunday 4 Part'),
        ('Sunday 4 Meeting', 'Sunday 4 Meeting'),
        ]
    date = str(datetime.date.today()) + ' 출석부'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True,
                             default=date)
    service_type = models.CharField(max_length=30, choices=SERVICE_TYPE, default='Saturday Worship')
    attend = models.BooleanField("출석 참여 여부", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)