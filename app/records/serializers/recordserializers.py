import datetime

from rest_framework import serializers

from members.models import User
from members.serializers.userserializers import UserSerializer
from ..models import Record, RecordResult


class RecordSerializer(serializers.ModelSerializer):
    # Test
    # user = UserSerializer(read_only=True, many=True)
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    # user 단독 유저 한병이면 어떻게 되는가
    user = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Record
        fields = ('id', 'title', 'user')

    def create(self, validated_data):
        record = Record.objects.create(**validated_data)
        return record


class RecordResultSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # record = serializers.PrimaryKeyRelatedField(queryset=Record.objects.all())
    user = UserSerializer(required=False, many=True)
    record = RecordSerializer(required=False)

    class Meta:
        model = RecordResult
        fields = ('user', 'record', 'service_type', 'pre_search', 'attend')

# class RecordSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     title = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
#     service_type = serializers.ChoiceField(choices=Record.SERVICE_TYPE, default='Saturday Worship')
#     pre_search = serializers.ChoiceField(choices=Record.PRE_SEARCH_TYPE, default='undefined')
#     attend = serializers.BooleanField(default=False)
#
#     def create(self, validated_data):
#         return Record.objects.create(**validated_data)


######################################
# update에서 각 user별 attend를 어떻게 설정해줘야 할지 고민해보자
# def update(self, instance, validated_data):
#
#     try:
#         instance.title = validated_data.get('title', instance.title)
#     except Exception as ex:
#         print('에러 발생, job ', ex)
#     try:
#         instance.service_type = validated_data.get('service_type', instance.service_type)
#     except Exception as ex:
#         print('에러 발생, job ', ex)
#     try:
#         instance.attend = validated_data.get('attend', instance.attend)
#     except Exception as ex:
#         print('에러 발생, job ', ex)
#
#     instance.save()
#     return instance


