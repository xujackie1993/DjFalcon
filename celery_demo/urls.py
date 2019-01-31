#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from .views import tasks

urlpatterns = [
    path('task', tasks, name='task'),
]
