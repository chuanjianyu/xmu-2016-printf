from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'roomManager.views.index', name = 'index'),
    url(r'^checkIn/$', 'roomManager.views.checkIn', name = 'checkIn'),

    #url(r'^checkIn/(?P<id>\d+)/$', 'roomManager.views.checkIn', name = 'checkIn'),
    url(r'^payBalance/$', 'roomManager.views.payBalance', name = 'payBalance'),
    url(r'^addalance/$', 'roomManager.views.addBalance', name = 'addBalance'),

    url(r'^queryCenter/$', 'roomManager.views.queryCenter', name = 'queryCenter'),
    url(r'^queryByRoomId/$', 'roomManager.views.queryByRoomId', name = 'queryByRoomId'),
    url(r'^queryByRoomType/$', 'roomManager.views.queryByRoomType', name = 'queryByRoomType'),
    url(r'^queryByBedType/$', 'roomManager.views.queryByBedType', name = 'queryByBedType'),
    url(r'^queryByFloorId/$', 'roomManager.views.queryByFloorId', name = 'queryByFloorId'),

    url(r'^myRoom/$', 'roomManager.views.myRoom', name = 'myRoom'),
    url(r'^checkOut/$', 'roomManager.views.checkOut', name = 'checkOut'),
    url(r'^deleteRoom/(?P<id>\d+)/$', 'roomManager.views.deleteRoom', name = 'deleteRoom'),
)
