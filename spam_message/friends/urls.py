from django.conf.urls import url
from friends import views

urlpatterns = [
    url(r'^search_friends/',views.search_friends),
    url(r'^send_friend_request/',views.send_friend_request),
    url(r'^manage_friend_request/',views.manage_friend_request),
    url(r'^view_friends_list/',views.view_friends_list),
    url(r'^chat_with_friends/',views.chat_with_friends),
    url(r'^send_request/(?P<abc>\w+)',views.send_request,name='abcdef'),
    url(r'^manage_friend_request/', views.manage_friend_request),
    url(r'^accept_friend/(?P<abc>\w+)',views.accept_friend,name='accept_friend'),
    url(r'^reject_friend/(?P<cdf>\w+)',views.reject_friend,name='reject_friend'),
    url(r'^search_result/',views.search_result),
    url(r'^search_send_request/(?P<df>\w+)',views.search_send_request,name='aaaaaaaaaa'),
    url('already_friend/',views.already_friend),
    url('view_blocked_friends/',views.view_blocked_friends,name='block_user'),
    # url('block_your_friends/', views.block_your_friends),

    ]
