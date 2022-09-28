# tweet/models.py
from django.db import models
from user.models import UserModel
from taggit.managers import TaggableManager


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    tags = TaggableManager(blank=True) # 비어있어도 작동한다
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)