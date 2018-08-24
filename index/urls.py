#!/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:李仲新 time:2018/8/14
from django.conf.urls import url
from django.urls import include
from .views import *


urlpatterns = [
    url(r'^login/$', login_views),
    url(r'^register/$', register_views),

    url(r'^oneindex/$', one_index_views),
    url(r'^index/$', index_views),
    url(r'^quit/$', quit_views),
]

urlpatterns += [
    url(r'^checkphone/$', checkphone_views)
]

urlpatterns += [
    url(r'', include('Crawl.urls'))
]
