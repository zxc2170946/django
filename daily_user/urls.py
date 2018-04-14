from django.conf.urls import  url
from . import views
urlpatterns=[
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login_handle/$',views.login_handle),
    url(r'^info/$',views.info),
    url(r'^user_center_site/$',views.site),
    url(r'^logout/$',views.logout),
    url(r'^site/$',views.site),
    url(r'^$',views.login),
    url(r'user_center_order&(\d+)/$',views.user_center_order)
]