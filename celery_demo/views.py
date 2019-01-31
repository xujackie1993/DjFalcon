#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import run_test_suit


def tasks(request):
    print("before run_test_suit")
    result = run_test_suit.delay('110')
    print("after run_test_suit")
    return HttpResponse("job is running backgroud~")
