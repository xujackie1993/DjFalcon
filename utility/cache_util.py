#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from django.core.cache import cache
from django.conf import settings


def write_to_cache(key, value, timeout=None):
    cache.set(key, json.dumps(value), timeout=timeout)


def read_from_cache(key):
    value = cache.get(key)
    if value is None:
        data = None
    else:
        data = json.loads(value)
    return data

