from django.conf import settings
from django.db import models

# from members.models import User


class Record(models.Model):
    title = models.CharField(max_length=50, unique=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='RecordResult', related_name='record_users')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class RecordResult(models.Model):
    SERVICE_TYPE = [
        ('Saturday Worship', 'Sunday 4 Part'),
        ('Sunday Part 1 Worship', 'Sunday 1 Part'),
        ('Sunday Part 2 Worship', 'Sunday 2 Part'),
        ('Sunday Part 3 Worship', 'Sunday 3 Part'),
        ('Sunday Part 4 Worship', 'Sunday 4 Part'),
        ('Sunday Meeting', 'Sunday Meeting'),
    ]
    PRE_SEARCH_TYPE = [
        ('참석', 'attendance'),
        ('불참', 'nonattendance'),
        ('미정', 'undefined'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='result_users', on_delete=models.SET_NULL, null=True)
    record = models.ForeignKey(Record, related_name='result_record', on_delete=models.SET_NULL, null=True)
    service_type = models.CharField(max_length=30, choices=SERVICE_TYPE, default='Saturday Worship')
    pre_search = models.CharField(max_length=30, choices=PRE_SEARCH_TYPE, default='undefined')
    attend = models.BooleanField("출석 참여 여부", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# class Record(models.Model):
#     SERVICE_TYPE = [
#         ('Saturday Worship', 'Sunday 4 Part'),
#         ('Sunday Part 1 Worship', 'Sunday 1 Part'),
#         ('Sunday Part 2 Worship', 'Sunday 2 Part'),
#         ('Sunday Part 3 Worship', 'Sunday 3 Part'),
#         ('Sunday Part 4 Worship', 'Sunday 4 Part'),
#         ('Sunday Meeting', 'Sunday Meeting'),
#     ]
#     PRE_SEARCH_TYPE = [
#         ('참석', 'attendance'),
#         ('불참', 'nonattendance'),
#         ('미정', 'undefined'),
#     ]
#
#     # date = str(datetime.date.today()) + ' 출석부'
#     # user = models.ForeignKey(User, related_name='user_record_set', on_delete=models.CASCADE)
#     user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='record_user_set')
#     title = models.CharField(max_length=50, unique=True)
#     service_type = models.CharField(max_length=30, choices=SERVICE_TYPE, default='Saturday Worship')
#     pre_search = models.CharField(max_length=30, choices=PRE_SEARCH_TYPE, default='undefined')
#     attend = models.BooleanField("출석 참여 여부", default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
