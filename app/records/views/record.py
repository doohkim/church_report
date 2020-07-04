from urllib.parse import urlparse

from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from members.models import User
from members.serializers.userserializers import UserSerializer
from ..serializers.recordserializers import RecordSerializer, RecordResultSerializer
from ..models import Record, RecordResult


class RecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def perform_create(self, serializer):
        if "title" in self.request.data:
            title = self.request.data['title']
            serializer.save(title=title)

        else:
            serializer.save()

        record = Record.objects.get(title=title)
        users = User.objects.all()
        for user in users:
            data = {}
            serializer = RecordResultSerializer(data=data)
            serializer.is_valid()
            serializer.save(record=record, user=user)


class RecordResultDetail(APIView):

    def get_object(self):
        title = self.kwargs['title']
        try:
            return Record.objects.get(title=title)
        except Record.DoesNotExist:
            raise Http404

    def get(self, request, format=None, **kwargs):
        # title = self.kwargs['title']
        # try:
        #     record = Record.objects.get(title=title)
        # except Record.DoesNotExist:
        #     raise Http404
        record = self.get_object()
        record_result = RecordResult.objects.filter(record_id=record.id)
        serializer = RecordResultSerializer(record_result, many=True)
        return Response(serializer.data)

    def put(self, request, format=None, **kwargs):
        record = self.get_object()
        record_result = RecordResult.objects.filter(record_id=record.id)
        serializer = RecordResultSerializer(record_result, data=request.data)




# class RecordResultDetail(generics.ListAPIView):
#     serializer_class = BasicRecordResultSerializer
#     queryset = RecordResult.objects.all()
#
#     def get_queryset(self):
#         title = self.kwargs['title']
#         # print(title)
#         record = get_object_or_404(Record, title=title)
#         queryset = RecordResult.objects.filter(record_id=record.id)
#         try:
#             queryset = RecordResult.objects.filter(record_id=record.id)
#         except RecordResult.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = BasicRecordResultSerializer(queryset, many=True)
#         return serializer

    # def get_object(self):
    #     title = self.kwargs['title']
    #     print(title)
    #     record = get_object_or_404(Record, title=title)
    #     queryset = self.filter_queryset(self.get_queryset())
    #     obj = queryset.filter(record_id=record.id)
    #     print(obj)
    #     return obj

