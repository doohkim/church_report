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
        # data['user'] = request.user
        data['user'] = User.objects.get(email=data['email']).id
        print("data:  ", data)

        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetailAPIView(APIView):

    def get_object(self,pk):
        try:
            # return UserProfile.objects.get(user=self.request.user)
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk,format=None):
        user = self.get_object(pk)
        print(user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        data = request.data
        #data['user'] = request.user
        data['user'] = pk
        # print("data:  ", data)
        serializer = UserProfileSerializer(user_profile, data=data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
