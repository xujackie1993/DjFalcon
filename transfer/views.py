#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.http import HttpResponse
from django_redis import get_redis_connection
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .models import Host, ServerRules
from .rrdtool_action import rrd_init_or_update

conn = get_redis_connection('default')


class HostReportView(APIView):
    permission_classes = []

    def post(self, request):
        if request.method == "POST":
            data = request.data
            print(data)
            cdn = data.get("cdn", None)
            try:
                server_rule = ServerRules.objects.get(Cdn=cdn)
            except Exception as e:
                return HttpResponse("ServerRule object does not exist error: ", e)
            hostname = data.get("hostname", None)
            ip_address = data.get("ip_address", None)
            mac_address = data.get("mac_address", None)
            os_type = data.get("os_type", None)
            os_version = data.get("os_version", None)
            internal_ip = ''
            external_ip = ''
            if ip_address:
                l_ips = ip_address.split(",")
                internal_ip = l_ips[0]
                if len(l_ips) > 1:
                    external_ip = l_ips[1]
            if Host.objects.filter(InternalIp=internal_ip, MacAddress=mac_address):
                Host.objects.update(Hostname=hostname, MacAddress=mac_address, InternalIp=internal_ip,
                                    ExternalIp=external_ip, OsType=os_type, OsVersion=os_version, Cdn=server_rule)
            else:
                Host.objects.create(Hostname=hostname, MacAddress=mac_address, InternalIp=internal_ip,
                                    ExternalIp=external_ip, OsType=os_type, OsVersion=os_version, Cdn=server_rule)
            return HttpResponse('add success! ', HTTP_200_OK)


class ItemCpuReportView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        hostname = data['host']['hostname']
        base_dir = os.path.join(settings.BASE_DIR, 'rrddatas')
        rrd_dir = os.path.join(base_dir, hostname)
        if not os.path.isdir(rrd_dir):
            os.makedirs(rrd_dir)
        for k, v in data['items'].items():
            rrd_name = k + '.rrd'
            rrd_init_or_update(rrd_name, v['value'], v['step'], v['counterType'], rrd_dir)
        return HttpResponse('insert success!!', HTTP_200_OK)


class ItemMemReportView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        hostname = data['host']['hostname']
        base_dir = os.path.join(settings.BASE_DIR, 'rrddatas')
        rrd_dir = os.path.join(base_dir, hostname)
        if not os.path.isdir(rrd_dir):
            os.makedirs(rrd_dir)
        for k, v in data['items'].items():
            rrd_name = k + '.rrd'
            rrd_init_or_update(rrd_name, v['value'], v['step'], v['counterType'], rrd_dir)
        return HttpResponse('insert success!!', HTTP_200_OK)


class ItemDataReportView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        hostname = data['host']['hostname']
        base_dir = os.path.join(settings.BASE_DIR, 'rrddatas')
        rrd_dir = os.path.join(base_dir, hostname)
        if not os.path.isdir(rrd_dir):
            os.makedirs(rrd_dir)
        for k, v in data['items'].items():
            rrd_name = k + '.rrd'
            rrd_init_or_update(rrd_name, v['value'], v['step'], v['counterType'], rrd_dir)
        return HttpResponse('insert success!!', HTTP_200_OK)


def index(request):
    context = {
        "hello": "Hello World"
    }
    return HttpResponse(context)
