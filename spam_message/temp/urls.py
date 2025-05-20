from django.conf.urls import url
from temp import views


urlpatterns = [
        url('userhome/',views.user_home),
        url('admin_home/',views.admin_home),
        url('login/',views.login)

]