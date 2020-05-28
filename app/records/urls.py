from django.urls import path

from records.views.record import RecordListCreateAPIView, RecordResultRetrieveUpdateDestroyAPIVew

urlpatterns = [
    path('', RecordListCreateAPIView.as_view()),
    path('result/<title>/', RecordResultRetrieveUpdateDestroyAPIVew.as_view()),
]