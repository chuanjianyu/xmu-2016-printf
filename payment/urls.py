#!/usr/bin/python
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
from django.contrib import admin
#from accounts import views
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^upgrade/(?P<acc_type>\w+)/$', 'payment.views.upgrade_account', name="payment_upgrade_account"),
    url(r'^upgrade/$', 'payment.views.upgrade_account', name="payment_upgrade_account"),
    url(r'^$', TemplateView.as_view(template_name='payment/plans.html'),name="payment_upgrade_plans"),
    url(r'^success/$', TemplateView.as_view(template_name= 'payment/success.html'), name="payment_success"),
    url(r'^error/$', TemplateView.as_view(template_name='payment/error.html'), name="payment_error"),
    url(r'^return_url/$', view = 'payment.views.return_url_handler', name="payment_return_url"),
    url(r'^notify_url/$', view = 'payment.views.notify_url_handler', name="payment_notify_url"),
)
