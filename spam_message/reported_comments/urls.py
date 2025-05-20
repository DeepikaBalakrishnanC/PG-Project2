from django.conf.urls import url
from reported_comments import views

urlpatterns = [
    url('view_cyberbullying_report/',views.view_cyberbullying_report),
    url('view_block/(?P<cdf>\w+)',views.view_block,name='block_user')

    ]


