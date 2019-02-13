#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse
from django_redis import get_redis_connection
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from .models import Host
from .rrdtool_action import convert_data_rrd
from utility.cache_util import get_inter_exter_mapping

conn = get_redis_connection('default')


class HostReportView(APIView):
    permission_classes = []

    def post(self, request):
        if request.method == "POST":
            data = request.data
            cdn = data.get("cdn", None)
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
                                    ExternalIp=external_ip, OsType=os_type, OsVersion=os_version, Cdn=cdn,
                                    UpdateTime=datetime.datetime.now())
            else:
                Host.objects.create(Hostname=hostname, MacAddress=mac_address, InternalIp=internal_ip,
                                    ExternalIp=external_ip, OsType=os_type, OsVersion=os_version, Cdn=cdn)
            return HttpResponse('add success! ', HTTP_200_OK)


class ItemCpuReportView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        internal_ip = data['host']
        ip_mapping = get_inter_exter_mapping()
        external_ip = ip_mapping.get(internal_ip, "unknown")
        convert_data_rrd(external_ip, data["items"])
        return HttpResponse('insert success!!', HTTP_200_OK)


class ItemMemReportView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        internal_ip = data['host']
        ip_mapping = get_inter_exter_mapping()
        external_ip = ip_mapping.get(internal_ip, "unknown")
        convert_data_rrd(external_ip, data["items"])
        return HttpResponse('insert success!!', HTTP_200_OK)


def index(request):
    context = {
        "hello": "Hello World"
    }
    return HttpResponse(context)
