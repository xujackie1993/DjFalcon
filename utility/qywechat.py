#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib.request
# from django_redis import get_redis_connection
#
# conn = get_redis_connection('default')


qyid = 'wweee9b021f3feeb8d'
# corpsecret = '8v_lxKurCwbutHvwY9d-2fFTuXlfsofDmhtJoSCJZ_8'
url = 'https://qyapi.weixin.qq.com'
msg = 'test2,Python调用企业微信测试2'

agentid = 1000003
corpsecret = 'SbR71YfMwyJkwuZAn7mnlYJhzY1-2oAArgyVAXFatq0'
corpsecret2 = '8v_lxKurCwbutHvwY9d-2fFTuXlfsofDmhtJoSCJZ_8'


# 构建告警信息json
def messages(msg):
    values = {
        "touser": '@all',
        "msgtype": 'text',
        "agentid": agentid,
        "text": {'content': msg},
        "safe": 0
        }
    msges = (bytes(json.dumps(values), 'utf-8'))
    return msges


# 获取企业微信token
def get_token(url, corpid, corpsecret):
    token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url, corpid, corpsecret)
    token = json.loads(urllib.request.urlopen(token_url).read().decode())['access_token']
    return token


# 发送告警信息
def send_message(url, corpid, corpsecret, msg):
    msg_data = messages(msg)
    token = get_token(url, corpid, corpsecret)

    send_url = '%s/cgi-bin/message/send?access_token=%s' % (url, token)
    respone = urllib.request.urlopen(urllib.request.Request(url=send_url, data=msg_data)).read()
    x = json.loads(respone.decode())['errcode']
    if x == 0:
        print('Succesfully')
    else:
        print('Failed')


if __name__ == "__main__":
    send_message(url, qyid, corpsecret, msg)
