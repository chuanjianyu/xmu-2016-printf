from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from accounts import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LM.views.home', name='home'),

    #url(r'^$', 'accounts.views.index', name = 'accounts_index'),
    url(r'^login/$','accounts.views.login', name = 'accounts_login'),
    url(r'^vipLogin/$','accounts.views.vipLogin', name = 'accounts_vipLogin'),
    url(r'^logout/$','accounts.views.logout', name = 'accounts_logout'),
    url(r'^updatepasswd/$','accounts.views.updatepasswd', name = 'accounts_updatepasswd'),

    url(r'^MyInf/$', 'accounts.views.MyInf', name = 'accounts_listMyInf'),
    url(r'^updateInf/$', 'accounts.views.updateInf', name = 'accounts_updateInf'),

    url(r'^addCompany/(?P<id>\d+)/$', 'accounts.views.addCompany', name = 'addCompany'),
    url(r'^listCompany/(?P<id>\d+)/$', 'accounts.views.listCompany', name = 'listCompany'),
)
