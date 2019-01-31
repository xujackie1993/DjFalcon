#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from django.core.cache import cache
from transfer.models import ServerRules, IpRules, Host


def set_cache(key, value, timeout=None):
    cache.set(key, json.dumps(value), timeout=timeout)


def get_cache(key):
    value = cache.get(key)
    if value is None:
        data = None
    else:
        data = json.loads(value)
    return data


def get_judge_rules(cdn, ip=None):
    rule = None
    if ip:
        ip_rule_cache = get_cache("rule_" + ip)
        if ip_rule_cache:
            ip_rule = ip_rule_cache
            return ip_rule
        else:
            ip_rule_obj = IpRules.objects.filter(ip=ip)
            if ip_rule_obj:
                ip_rule = ip_rule_obj[0].ip_rule_dict
                set_cache("rule_" + ip, ip_rule)
                return ip_rule
    else:
        cdn_rule_cache = get_cache("rule_" + cdn)
        if cdn_rule_cache:
            cdn_rule = cdn_rule_cache
            return cdn_rule
        else:
            cdn_rule_obj = ServerRules.objects.filter(Cdn=cdn)
            if cdn_rule_obj:
                cdn_rule = cdn_rule_obj[0].ip_rule_dict
                set_cache("rule_" + cdn, cdn_rule)
                return cdn_rule
    return rule


def get_inter_exter_mapping():
    d_mapping = get_cache("inner_exter_mapping")
    if d_mapping:
        return d_mapping
    d_result = {}
    hosts = Host.objects.all()
    for host in hosts:
        host_dict = host.inter_exter_dict
        d_result[host_dict['internal_ip']] = host_dict['external_ip']
    set_cache("inner_exter_mapping", d_result)
    return d_result




