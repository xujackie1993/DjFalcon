#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from rest_framework.renderers import JSONRenderer


class CustomJsonRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        格式
        {
            'code': xxx,
            'msg': 请求成功.
            data: {返回数据}
        }

        """
        if renderer_context:                        # ---> renderer_context 如果有内容:
            if "detail" in json.dumps(data, ensure_ascii=True):
                msg = "请求失败"
                code = 1
            else:
                if isinstance(data, dict):              # --->推断data是否是dict类型
                    msg = data.pop('msg', '请求成功')    # --->如果有msg,删除键,返回值,命名msg=值,没有msg键,命名msg = '请求成功',
                    # pop(删除的键, 没有键返回的默认值)
                    code = data.pop('code', 0)          # --->如果有code,删除code键, 返回值,命名code=值, 如果没有code键,则重新命名code = '0'
                else:
                    msg = '请求成功'
                    code = 0
            response = renderer_context['response']  # ---> 获取response信息
            response.status_code = 200               # ---> 将response.ststus_code, 如果请求成功的全部返回200的状态码
            res = {
                'code': code,
                'msg': msg,
                'data': data
            }
            return super().render(res, accepted_media_type, renderer_context)  # --->调用父类的render方法,和跳转的render不是一个方法, 下同
        else:
            return super().render(data, accepted_media_type, renderer_context)
