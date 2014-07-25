#coding: utf-8
from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
                       
url(r'^$', views.login_views, name='list'),                                               
#url(r'^(?P<pk>\d+)/$', views.login_views , name='list'),
url(r'^login/$',  views.login),
url(r'^logout/$', views.logout),
url(r'^reg_user_token/$', views.reg_user_token),
url(r'^xml_res_pagin/$', views.xml_res_pagin),
url(r'^delete_user/$', views.delete_user), 
url(r'^api_filtr/$', views.api_filtr),   
                   
)
