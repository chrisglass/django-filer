#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
#from django.conf.urls.static import static
#from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/filer_private/', include('filer.server.urls')),
)