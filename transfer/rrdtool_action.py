# -*- coding:utf-8 -*-

import os
import time
import rrdtool
from django.conf import settings


def rrd_init(rrd_name, step, counter_type):
    """
    聚合时间根据自己需要
    """
    cur_time = str(int(time.time()))

    # RRA定义格式为[RRA:CF:xff:steps:rows]，CF定义了AVERAGE、MAX、MIN三种数据合并方式
    # xff定义为0.5，表示一个CDP中的PDP值如超过一半值为UNKNOWN，则该CDP的值就被标为UNKNOWN
    # 下列前4个RRA的定义说明如下，其他定义与AVERAGE方式相似，区别是存最大值与最小值
    # 每隔5分钟(1*300秒)存一次数据的平均值,存600笔，即2.08天
    # 每隔30分钟(6*300秒)存一次数据的平均值,存700笔，即14.58天（2周）
    # 每隔2小时(24*300秒)存一次数据的平均值,存775笔，即64.58天（2个月）
    # 每隔24小时(288*300秒)存一次数据的平均值,存797笔，即797天(2年)

    rrd = rrdtool.create(rrd_name, '--step', '%s' % step, '--start', cur_time,
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
        print(rrd.error())


def rrd_update(rrd_name, rx):
    start_time = int(time.time())
    print(rrd_name, start_time, type(start_time), rx, type(rx))
    x = rrdtool.updatev(rrd_name, "%s:%s" % (str(start_time), str(rx)))
    if x:
        print(x.error())


def rrd_init_or_update(rrd_name, value, step, counter_type, rrd_dir):
    rrd_path = os.path.join(rrd_dir, rrd_name)
    if os.path.isfile(rrd_path):
        rrd_update(rrd_path, value)
    else:
        rrd_init(rrd_path, step, counter_type)
        rrd_update(rrd_path, value)


def convert_data_rrd(host, items):
    base_dir = os.path.join(settings.BASE_DIR, 'rrddatas')
    rrd_dir = os.path.join(base_dir, host)
    if not os.path.isdir(rrd_dir):
        os.makedirs(rrd_dir)
    for k, v in items.items():
        rrd_name = k + '.rrd'
        rrd_init_or_update(rrd_name, v['value'], v['step'], v['counterType'], rrd_dir)