from django.urls import path

from members.views.userprofile import UserProfileListCreateAPIView, UserProfileDetailAPIView
from .views.user import UserListCreateAPIView, UserDetailAPIView

urlpatterns = [
    path('',  UserListCreateAPIView.as_view()),
    path('<int:pk>/', UserDetailAPIView.as_view()),
    path('profile/', UserProfileListCreateAPIView.as_view()),
    path('profile/<int:pk>/', UserProfileDetailAPIView.as_view()),
]