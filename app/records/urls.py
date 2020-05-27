from django.urls import path

from records.views.record import RecordListCreateAPIView, RecordResultCreateAPIView

urlpatterns = [
    path('', RecordListCreateAPIView.as_view()),
    path('result/', RecordResultCreateAPIView.as_view()),
]