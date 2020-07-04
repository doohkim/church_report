import datetime

from rest_framework import serializers

from members.models import User
from members.serializers.userserializers import UserSerializer
from ..models import Record, RecordResult


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'title',)

    def create(self, validated_data):
        record = Record.objects.create(**validated_data)
        return record
    # def create(self, validated_data):
    #     record = Record.objects.create(**validated_data)
    #     users = User.objects.all()
    #     for user in users:
    #         RecordResult.objects.create(record=record, user=user)

# class UserListingField(serializers.RelatedField):
#     def to_representation(self, value):
#         data = {
#             "username" : value.name,
#             "attend"   : value.attend
#         }
#         return data


class RecordResultSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    record = RecordSerializer(required=False)

    class Meta:
        model = RecordResult
        fields = ('user', 'record', 'service_type', 'pre_search', 'attend')

    # 보통 to_representation은 보여준다 자기 자신의 정보를
    # def to_representation(self, instance):
    #     return UserSerializer(instance).data

