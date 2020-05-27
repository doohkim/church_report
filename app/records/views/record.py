from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from ..serializers.recordserializers import RecordSerializer, RecordResultSerializer
from ..models import Record, RecordResult


class RecordListCreateAPIView(APIView):
    def get(self, request, format=None):
        record = Record.objects.all()
        serializer = RecordSerializer(record, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        # data['user'] = User.objects.all()
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            # serializer.save(user=User.objects.first())
            serializer.save(user=User.objects.all())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecordResultCreateAPIView(APIView):
    def get(self, request, format=None):
        record_result = RecordResult.objects.all()
        # user = User.objects.all()
        serializer = RecordResultSerializer(record_result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        pass