from urllib.parse import urlparse

from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from members.models import User
from members.serializers.userserializers import UserSerializer
from ..serializers.recordserializers import RecordSerializer, RecordResultSerializer
from ..models import Record, RecordResult


# class RecordListCreateAPIView(APIView):
#     def get(self, request, format=None):
#         record = Record.objects.all()
#         serializer = RecordSerializer(record, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         data = request.data
#         print(data)
#         # data['user'] = User.objects.all()
#         serializer = RecordSerializer(data=data)
#         if serializer.is_valid():
#             # serializer.save(user=User.objects.first())
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            data ={}
            serializer = RecordResultSerializer(data=data)
            serializer.is_valid()
            serializer.save(record=record, user=user)


class RecordResultRetrieveUpdateDestroyAPIVew(generics.ListCreateAPIView):
    # queryset = RecordResult.objects.all()
    # serializer_class = RecordResultSerializer

    def get_queryset(self):
        title = urlparse(self.kwargs['title'])
        record, _ = Record.objects.get_or_create(title=title)
        if title is not None:
            queryset = RecordResult.objects.filter(record=record)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecordResultSerializer
        elif self.request.method == 'POST':
            return RecordResultSerializer






























        # def perform_create(self, serializer):
    #     title = urlparse(self.kwargs['title'])
    #     print(title)
    #     record, _ = Record.objects.get_or_create(title=title)
    #     print(record)
    #     user = self.request.user
    #     print(user)
    #     RecordResultSerializer.save(record=record, user=user)

    # class RecordResultCreateAPIView(APIView):
    #     def get_object(self, title):
    #         try:
    #             return Record.objects.get(title=title)
    #         except Record.DoesNotExist:
    #             raise Http404
    #
    #     def get(self, request, title, format=None):
    #         user = User
    #
    #         serializer = RecordResultSerializer()
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, title, format=None):
    #     record = RecordResult.objects.get(title=request.data['title'])
    #     # users = User.objects.all()
    #     for user in request.data.getlist('users'):
    #         data = {
    #             "title" : request.data['title'],
    #             "user" : user
    #         }
    #         serializer = RecordResultSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #         else:
    #             return Response(serializer.errors)
    #     serializer =
    #     return Response(serializer.data)

    # class PostImageCreateAPIView(APIView):
    """
    PostImageCreateSerializer를 사용하도록 구현
    """

    # def post(self, request, pk):
    #     post = Post.objects.get(pk=pk)
    #     for image in request.data.getlist('image'):
    #         data = {'image': image}
    #         serializer = PostImageCreateSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save(post=post)
    #         else:
    #             return Response(serializer.errors)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
