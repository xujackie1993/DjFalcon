#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from transfer.views import index, HostReportView, ItemCpuReportView

urlpatterns = [
    path('hello', index, name='index'),
    path('item/host', HostReportView.as_view(), name='item_host'),
    path('item/cpu', ItemCpuReportView.as_view(), name='item_cpu')
]
