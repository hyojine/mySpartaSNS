# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 그냥 http://127.0.0.1:8000/일때는 view안의 home이란 함수를 보여준다
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('tweet/', views.tweet, name='tweet'),  # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete-tweet'),
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]
