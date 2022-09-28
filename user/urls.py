# user앱과 관련된 url을 모두 여기 작성
# sparta sns .. 연결해줘야함
from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    # url 만들어짐, 뷰파일의 --뷰가 실행저 함수가 어느페이지를 보여주는지 쓰여있음,
    path('logout/', views.logout, name='logout'),
    path('user/',views.user_view,name='user-list'),
    path('user/follow/<int:id>/',views.user_follow,name='user-follow'),
]
