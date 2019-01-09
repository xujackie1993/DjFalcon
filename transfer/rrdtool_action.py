# -*- coding:utf-8 -*-

import os
import time

import rrdtool


def rrd_init_or_update(rrd_name, value, step, counter_type, rrd_dir):
    rrd_path = os.path.join(rrd_dir, rrd_name)
    if os.path.isfile(rrd_path):
        rrd_update(rrd_path, value)
    else:
        rrd_init(rrd_path, step, counter_type)
        rrd_update(rrd_path, value)


def rrd_init(rrdname, step, counter_type):
    """
    聚合时间根据自己需要
    """
    cur_time = str(int(time.time()))
    rrd = rrdtool.create(rrdname, '--step', '%s' % step, '--start', cur_time,
                         'DS:metric:%s:600:0:U' % counter_type,
                         'RRA:AVERAGE:0.5:1:600',
                         'RRA:AVERAGE:0.5:6:700',
                         'RRA:AVERAGE:0.5:24:775',
                         'RRA:AVERAGE:0.5:288:797',
                         'RRA:MAX:0.5:1:600',
                         'RRA:MAX:0.5:6:700',
                         'RRA:MAX:0.5:24:775',
                         'RRA:MAX:0.5:444:797',
                         'RRA:MIN:0.5:1:600',
                         'RRA:MIN:0.5:6:700',
                         'RRA:MIN:0.5:24:775',
                         'RRA:MIN:0.5:444:797',
                         )

    if rrd:
        print(rrd)


def rrd_update(rrd_name, rx):
    start_time = int(time.time())
    print(rrd_name, start_time, type(start_time), rx, type(rx))
    x = rrdtool.updatev(rrd_name, "%s:%s" % (str(start_time), str(rx)))
    if x:
        print(x)
