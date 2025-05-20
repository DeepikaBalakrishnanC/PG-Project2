from django.conf.urls import url
from chat import views

urlpatterns = [
    url('chat/(?P<abc>\w+)',views.chat,name='chat'),
    url('chat_with_friends/',views.chat_with_friends),
    url('view_chat/',views.view_chat)

]
