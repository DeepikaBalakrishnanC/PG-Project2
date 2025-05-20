from django.conf.urls import url
from user_reg import views

urlpatterns=[
    url('user_reg/',views.user_reg),
    url('manage_user/',views.manage_user),
    url('view_blocked_user/',views.view_blocked_user),
    url('admin_view_user/',views.admin_view_user),
    url('approve_user/(?P<abc>\w+)',views.approve_user,name='approve_user'),
    url('reject_user/(?P<cdf>\w+)',views.reject_user,name='reject_user'),
    url('blkuser/(?P<idd>\w+)',views.blckuser,name='blkuser'),
    url('edit_profile/',views.edit_profile),
    url('edit_username/',views.edit_username),
    url('edit_email/',views.edit_email),
    url('edit_password/',views.edit_password),
    url('edit_phno/',views.edit_phno),
    url('admin_view_blocked_users/',views.admin_view_blocked_users),
    url('unblock/(?P<aa>\w+)',views.unblock,name='unblock')
]
