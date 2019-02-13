#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transfer.models import CpuAlarmRules, Host, DiskAlarmRules, MemoryAlarmRules
from .serializers import CpuAlarmRulesSerializer, HostSerializer, DiskAlarmRulesSerializer, MemoryAlarmRulesSerializer
from rest_framework import mixins, viewsets
from django_filters import rest_framework as filters


class HostFilter(filters.FilterSet):
    class Meta:
        model = Host
        fields = ["Hostname", "MacAddress", "ExternalIp", "InternalIp", "OsType", "OsVersion", "Cdn", "ChannelGroup"]


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class CpuFilter(filters.FilterSet):
    class Meta:
        model = CpuAlarmRules
        fields = ["Name", "CpuAlarmLevel", "Ip", "Cdn", "ChannelGroup"]


class CpuViewSet(viewsets.ModelViewSet):
    queryset = CpuAlarmRules.objects.all()
    serializer_class = CpuAlarmRulesSerializer


class MemoryFilter(filters.FilterSet):
    class Meta:
        model = MemoryAlarmRules
        fields = ["Name", "MemoryAlarmLevel", "Ip", "Cdn", "ChannelGroup"]


class MemoryViewSet(viewsets.ModelViewSet):
    queryset = MemoryAlarmRules.objects.all()
    serializer_class = MemoryAlarmRulesSerializer


class DiskFilter(filters.FilterSet):
    class Meta:
        model = DiskAlarmRules
        fields = ["Name", "DiskAlarmLevel", "Ip", "Cdn", "ChannelGroup"]


class DiskViewSet(viewsets.ModelViewSet):
    queryset = DiskAlarmRules.objects.all()
    serializer_class = DiskAlarmRulesSerializer

#
# @api_view(['POST'])
# def add_cpu_rule(request):
#     data = JSONParser().parse(request)
#     serializer = CpuAlarmRulesSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         # serializer.data 数据创建成功后所有数据
#         return JsonResponse({"detail": serializer.data, "code": 0, "msg": "success"}, status=status.HTTP_200_OK)
#     # serializer.errors 错误信息
#     return JsonResponse({"detail": {}, "code": 1, "msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
