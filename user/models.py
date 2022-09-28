#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#장고가 관리하는 myspartasns/settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    bio = models.TextField(max_length=500, blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
    # auth_user_model은 우리 클래스 usermodel(사용자가 팔로우하는건 우리모델의 사용자들이니까)
