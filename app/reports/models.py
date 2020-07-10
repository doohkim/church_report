from django.db import models

from members.models import User


class Report(models.Model):
    SERVICE_TYPE = [
        ('토요일 예배 참석', '토요일 예배 참석'),
        ('주일 예배 참석', '주일 예배 참석'),
        ('주일 모임 참석', '주일 모임 참석'),
    ]
    PRE_SEARCH_TYPE = [
        ('참석', '참석'),
        ('불참', '불참'),
        ('미정', '미'),
    ]

    title = models.CharField(max_length=100, help_text='보고서 이름')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class RecordResult(models.Model):
    record = models.OneToOneField(Report, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attend = models.BooleanField("출석 참여 여부", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)