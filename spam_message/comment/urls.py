from django.conf.urls import url
from comment import views


urlpatterns = [
    url('comment/(?P<cid>\w+)',views.comment,name='com')

]
