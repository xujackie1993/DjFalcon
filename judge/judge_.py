#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc
import logging
from pprint import PrettyPrinter
from utility.cache_util import get_judge_rules

logger = logging.getLogger(__name__)
printer = PrettyPrinter(indent=1, width=130)


class JudgeBase(metaclass=abc.ABCMeta):

    def __init__(self, data):
        super(JudgeBase, self).__init__()
        self.logger = logger
        self.ip = data.get("ip")
        self.cdn = data.get("cdn")
        self.judge_rule = get_judge_rules(self.cdn, self.ip)

    @abc.abstractmethod
    def judge_alarm(self, threshold, value):
        raise NotImplemented

    def compared_log(self, th, va):
        message = "[compared] %s %s" % (printer.pformat(th), printer.pformat(va))
        self.logger.info(message)


class JudgeCpu(JudgeBase):
    def __init__(self):
        super(JudgeCpu, self).__init__()

    def judge_alarm(self, threshold, value):
        pass
