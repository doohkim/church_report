from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from records.models import Record
from records.serializers.recordserializers import RecordSerializer, RecordResultSerializer


class RecordListCreateAPIView(APIView):
    def get(self, request, format=None):
        record = Record.objects.all()
        serializer = RecordSerializer(record, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if "title" in self.request.data:
            serializer = RecordSerializer(data=request.data)
            serializer.save()

        else:
            serializer = RecordSerializer()
            serializer.save()
        title = request.data['title']
        record = Record.objects.get(title=title)
        users = User.objects.all()
        for user in users:
            data = {}
            serializer = RecordResultSerializer(data=data)
            if serializer.is_valid():
                serializer.save(record=record, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)









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
