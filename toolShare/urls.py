""" 
file: urls.py
language: python3
author: Nicholas James 
description: Handles all of the urls in toolShare
"""

from django.conf.urls import patterns, include, url
from users.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toolShare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login', name = 'login'),
	url(r'^$', 'django.contrib.auth.views.logout', name = 'logout'),
	url(r'^register/$', 'users.views.RegisterView', name = 'register'),
	url(r'^home/$', 'users.views.home', name = 'home'),
	url(r'^mytools/$', 'users.views.mytools', name = 'mytools'),
	url(r'^mysheds/$', 'users.views.mysheds', name = 'mysheds'),
	url(r'^myprofile/$', 'users.views.myprofile', name = 'myprofile'),
	url(r'^createTool/$', 'users.views.toolCreate', name='createTool'),
	url(r'^createShed/$', 'users.views.shedCreate', name='createShed'),
	url(r'^about/$', 'users.views.about', name = 'about'),
	url(r'^contact/$', 'users.views.contact', name = 'contact'),
	url(r'^changePassword/$', 'users.views.changePassword',	name = 'changePassword'),
	url(r'^logout/$', 'users.views.UserLogout', name = 'logout'),
	url(r'^requestTool/(?P<tool_id>\d+)/$', 'users.views.requestTool', name='requestTool'),
	url(r'^returnTool/(?P<tool_id>\d+)/$', 'users.views.returnTool', name='returnTool'),
    url(r'^deleteTool/(?P<tool_id>\d+)/$', 'users.views.deleteTool', name='deleteTool'),
    url(r'^changeShed/(?P<shed_id>\d+)/$', 'users.views.changeShed', name='changeShed'),
    url(r'^editTool/(?P<tool_id>\d+)/', 'users.views.editTool', name='editTool'),
    url(r'^deleteShed/(?P<shed_id>\d+)/', 'users.views.deleteShed', name='deleteShed'),
    url(r'^messages/', include('postman.urls'), name='messages'),
    url(r'^search/$', 'users.views.searchSheds',name='search'),
    url(r'^searchTools/$', 'users.views.searchTools',name='searchTools'),
    url(r'^Terms/$', 'users.views.terms',name='Terms'),
    )

