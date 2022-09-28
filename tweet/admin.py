from django.contrib import admin
from .models import TweetModel

# Register your models here.
admin.site.register(TweetModel)
# TweetModel을 어드민에 등록해주겠다