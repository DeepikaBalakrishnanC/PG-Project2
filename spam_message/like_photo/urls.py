from django.conf.urls import url
from like_photo import views

urlpatterns = [
    url('like_photo/(?P<idd>\w+)', views.like, name='like')


]
