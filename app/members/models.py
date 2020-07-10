from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_img_dir(instance, filename):
    return '/'.join(['avatars', f'{instance.username}-{filename}'])


class User(AbstractUser):
    class Meta:
        verbose_name = '유저'
        verbose_name_plural = '유저'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=13, help_text='핸드폰 번호', blank=True)
    address = models.TextField(help_text='주소')
    avatar = models.ImageField(
        upload_to=profile_img_dir, blank=True, help_text='프로필 사진')

# class Favorite(models.Model):
#     user = models.ForeignKey(
#         'User', on_delete=models.CASCADE)
#     store = models.ForeignKey(
#         Store, related_name='favorites', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = '좋아요'
#         verbose_name_plural = '좋아요'
