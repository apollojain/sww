from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	# ex: /
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^signup/$', views.create, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.index, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='event_detail'),
    url(r'^toggle/(?P<event_id>[0-9]+)/$', views.toggle, name='toggle'),
    
]