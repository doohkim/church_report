from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.userprofileserializers import UserProfileSerializer
# from ..serializers.userserializers import UserSerializer
from ..models import User, UserProfile


class UserProfileListCreateAPIView(APIView):
    # 유저 전체 보여주기
    def get(self, request, format=None):
        users_profile = UserProfile.objects.all()
        serializer = UserProfileSerializer(users_profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        # data['user'] = request.user.id
        data['user'] = User.objects.get(email=data['email']).id
        print("data:  ", data)

        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            # return UserProfile.objects.get(user=self.request.user)
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print('request.user: ', request.user)
        user = self.get_object(pk)
        # print(user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        data = request.data
        # data['user'] = request.user.id
        data['user'] = pk
        # print("data:  ", data)
        serializer = UserProfileSerializer(user_profile, data=data, partial=True)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
























#
#
#
#
# from datetime import datetime
#
# class Comment(object):
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()
#
# comment = Comment(email='leila@example.com', content='foo bar')
#


