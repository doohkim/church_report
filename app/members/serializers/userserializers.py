import datetime

from django.utils import timezone
from rest_framework import serializers

# 유저 list view 만들꺼임
from ..models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True, allow_blank=False)
    name = serializers.CharField(max_length=30, allow_blank=True)
    is_superuser = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    recent_attend_date = serializers.DateField(
        default=datetime.date.today,
        format='%Y-%m-%d',
        input_formats=['%Y-%m-%d', 'iso-8601'])

    # created = serializers.DateTimeField()
    # updated = serializers.DateTimeField()

    def create(self, validated_data):
        print("validation: ", validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        try:
            instance.email = validated_data.get('email', instance.email)
            instance.name = validated_data.get('name', instance.name)
        except Exception as ex:
            print('에러 발생', ex)
        # print(validated_data.get('recent_attend_date', instance.recent_attend_date))
        instance.recent_attend_date = validated_data.get('recent_attend_date', instance.recent_attend_date)
        return instance

# def create(self, validated_data):
#     return User.objects.create(
#         username=validated_data['username'],
#         email=validated_data['email'],
#         is_premium_member=validated_data['profile']['is_premium_member'],
#         has_support_contract=validated_data['profile']['has_support_contract']
#     )