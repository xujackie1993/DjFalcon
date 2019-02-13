#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from web import views

router = DefaultRouter()
router.register(r'host', views.HostViewSet)
router.register(r'cpu', views.CpuViewSet),
router.register(r'memory', views.MemoryViewSet),
router.register(r'disk', views.DiskViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]
