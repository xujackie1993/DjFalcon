#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from transfer.models import CpuAlarmRules, MemoryAlarmRules, DiskAlarmRules, Host

# 序列化


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

    def to_representation(self, instance):     # 重写to_representation方法，把需要的字段加入返回的数据中
        data = super().to_representation(instance)
        try:
            pass
        except Exception as e:
            pass
        return data


class CpuAlarmRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuAlarmRules
        fields = '__all__'


class MemoryAlarmRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryAlarmRules
        fields = '__all__'


class DiskAlarmRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiskAlarmRules
        fields = '__all__'



