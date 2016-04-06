from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ServiceManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'roomManager.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^payment/', include('payment.urls', namespace = 'payment')),
    url(r'^accounts/', include('accounts.urls', namespace = 'accounts')),
    url(r'^roomManager/', include('roomManager.urls', namespace = "roomManager")),
)
