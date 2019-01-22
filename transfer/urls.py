#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from transfer.views import ItemDataReportView, HostReportView, index

urlpatterns = [
    path('hello', index, name='index'),
    path('host/report', HostReportView.as_view(), name='host_report'),
    path('item/report', ItemDataReportView.as_view(), name='item_report')
]
