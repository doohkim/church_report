import datetime

from django.utils import timezone
from rest_framework import serializers

# 유저 list view 만들꺼임
from members.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True, allow_blank=False)
    name = serializers.CharField(max_length=30, allow_blank=True)
    is_superuser = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    recent_attend_date = serializers.DateField(default=datetime.date.today)
    # created = serializers.DateTimeField()
    # updated = serializers.DateTimeField()

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.recent_attend_date = validated_data.get('recent_attend_date', instance.recent_attend_date)
    #     return instance
