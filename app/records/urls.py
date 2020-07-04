from django.urls import path

from records.views.record import *

urlpatterns = [
    path('', RecordListCreateAPIView.as_view()),
    path('result/<title>/', RecordResultDetail.as_view()),
]