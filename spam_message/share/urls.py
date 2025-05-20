from django.conf.urls import url
from share import views

urlpatterns = [
    url('share_photo/',views.share_photo),
    url('news_feed/',views.news_feed),
    url('view_post',views.view_post),
    url('view_comments/(?P<idd>\w+)', views.view_comments, name='commm'),
    url(r'^share_del/(?P<idd>\w+)', views.share_del, name='share_del'),
    # url('block_friend/(?P<ab>\w+)',views.block_friend, name='blockk')




]
