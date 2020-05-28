import datetime

from rest_framework import serializers

from members.models import User
from members.serializers.userserializers import UserSerializer
from ..models import Record, RecordResult


class RecordSerializer(serializers.ModelSerializer):
    # Test
    # user = UserSerializer(read_only=True, many=True)
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Record
        fields = ('id', 'title',)

    def create(self, validated_data):
        record = Record.objects.create(**validated_data)
        return record


class RecordResultSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    record = RecordSerializer(required=False)

    class Meta:
        model = RecordResult
        fields = ('user', 'record', 'service_type', 'pre_search', 'attend')

    def to_representation(self, instance):
        return UserSerializer(instance).data














        # class BookListSerializer(serializers.ListSerializer):
    #     def create(self, validated_data):
    #         books = [Book(**item) for item in validated_data]
    #         return Book.objects.bulk_create(books)
    #
    # class BookSerializer(serializers.Serializer):
    #     ...
    #
    #     class Meta:
    #         list_serializer_class = BookListSerializer
    #
    # class ProfileFeedItemListSerializer(serializers.ListSerializer):
    #     def create(self, validated_data):
    #         feed_list = [ProfileFeedItem(**item) for item in validated_data]
    #         return ProfileFeedItem.objects.bulk_create(feed_list)
    #
    # class ProfileFeedItemSerializer(serializers.ModelSerializer):
    #     """A serializer for profile feed items."""
    #
    #     class Meta:
    #         model = models.ProfileFeedItem
    #         list_serializer_class = ProfileFeedItemListSerializer
    #         fields = ('id', 'user_profile', 'status_text', 'created_on')
    #         extra_kwargs = {'user_profile': {'read_only': True}}

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
