import datetime

from phonenumber_field.phonenumber import to_python
from phonenumber_field.validators import validate_international_phonenumber
from rest_framework import serializers
from ..models import User, UserProfile


class UserProfileSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    job = serializers.CharField(required=False, max_length=50,
                                allow_null=True, allow_blank=True, default='정보없음')
    sex = serializers.ChoiceField(choices=UserProfile.SEX, default='Male')
    phone_number = serializers.CharField(validators=[validate_international_phonenumber], allow_blank=True,
                                         allow_null=True, required=False)
    age = serializers.IntegerField(allow_null=True, required=False, default=20)
    address = serializers.CharField(max_length=255, allow_null=True,
                                    allow_blank=True, default='정보없음')
    email_confirmed = serializers.BooleanField(default=False)
    recent_attend_date = serializers.DateField(
        default=datetime.date.today,
        format='%Y-%m-%d',
        input_formats=['%Y-%m-%d', 'iso-8601']
    )

    def create(self, validated_data):
        print("validated_data: ", validated_data)
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.user = User.objects.get(
        #     pk=validated_data.get('pk', instance.pk)
        #                                 )
        print('validated_data', validated_data)
        print(validated_data.get('job', instance.job))
        try:

            instance.job = validated_data.get('job', instance.job)
        except Exception as ex:
            print('에러 발생, job ', ex)
        try:

            instance.job = validated_data.get('job', instance.job)
        except Exception as ex:
            print('에러 발생, job ', ex)
        try:

            instance.sex = validated_data.get('sex', instance.sex)
        except Exception as ex:
            print('에러 발생 sex', ex)
        try:

            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        except Exception as ex:
            print('에러 발생 phone_number', ex)
        try:

            instance.address = validated_data.get('address', instance.address)
        except Exception as ex:
            print('에러 발생 address', ex)
        try:

            instance.recent_attend_date = validated_data.get('recent_attend_date', instance.recent_attend_date)
        except Exception as ex:
            print('에러 발생 recent_attend_date', ex)
        # try:
        #
        #     instance.email_confirmed = validated_data.get('email_confirmed', instance.email_confirmed)
        # except Exception as ex:
        #     print('에러 발생 email_confirmed', ex)

        instance.save()
        return instance
