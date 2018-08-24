#!/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:李仲新 time:2018/8/22
from django.conf.urls import url
from .views import *

urlpatterns = [
  url(r'^search/$', search_view)
]