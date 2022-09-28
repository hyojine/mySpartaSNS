"""mySpartaSns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  # views파일을 가져오겠다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tffkfkdi1/',views.base_response, name='first_test'),
    path('first/',views.first_view,name='first_view'),
    path('',include('user.urls')), #user의 url과 spartasns의 url과 연결
    path('',include('tweet.urls')),
]
