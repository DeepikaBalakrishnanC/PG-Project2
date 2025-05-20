"""spam_message URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('chat/', include('chat.urls')),
    url('comment/', include('comment.urls')),
    url('friends/', include('friends.urls')),
    url('like_photo/', include('like_photo.urls')),
    url('login/', include('login.urls')),
    url('reported_comments/', include('reported_comments.urls')),
    url('share/', include('share.urls')),
    url('user_reg/', include('user_reg.urls')),
    url('temp/', include('temp.urls')),
    url('$', views.login),
]
