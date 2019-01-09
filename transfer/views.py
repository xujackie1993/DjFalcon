#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .rrdtool_action import rrd_init_or_update


class ItemDataReportView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        hostname = data['host']['hostname']
        base_dir = os.path.join(settings.BASE_DIR, 'rrddatas')
        rrd_dir = os.path.join(base_dir, hostname)
        if not os.path.isdir(rrd_dir):
            os.mkdir(rrd_dir)
        for k, v in data['items'].items():
            rrd_name = k + '.rrd'
            rrd_init_or_update(rrd_name, v['value'], v['step'], v['counterType'], rrd_dir)
        return HttpResponse('insert success!!', HTTP_200_OK)


def index(request):
    context = {
        "hello": "Hello World"
    }
    return HttpResponse(context)
