from __future__ import unicode_literals
import datetime
from django.db import models
from django.core.cache import cache

ALARM_LEVEL = (
        (1, "邮件报警"),
        (2, "邮件加微信报警"),
        (3, "待定")
    )

Switch = (
    (1, "开"),
    (0, "关")
)


class CpuAlarmRules(models.Model):

    Name = models.CharField(max_length=40, verbose_name="cpu报警规则名称")
    CpuAlarmLevel = models.IntegerField(choices=ALARM_LEVEL, verbose_name="cpu报警级别")
    CpuAlarmTitle = models.CharField(max_length=40, verbose_name="cpu报警标题")
    TotalCpuUsageThreshold = models.IntegerField(verbose_name="总cpu报警阈值")
    SingleCpuUsageThreshold = models.IntegerField(verbose_name="单个cpu报警阈值")
    Ip = models.CharField(max_length=16, null=True, unique=True, verbose_name="ip地址")
    Cdn = models.CharField(max_length=24, null=True, verbose_name="cdn")
    ChannelGroup = models.CharField(max_length=24, null=True, verbose_name="频道组")

    class Meta:
        db_table = "cpu_alarm_rules"
        verbose_name = "cpu报警规则"

    def save(self, *args, **kwargs):
        cache.delete("cpu_alarm_rules_" + self.Ip)
        super(CpuAlarmRules, self).save(*args, **kwargs)

    @property
    def dict_data(self):
        return {
            "name": self.Name,
            "cpu_alarm_level": self.CpuAlarmLevel,
            "cpu_alarm_title": self.CpuAlarmTitle,
            "total_cpu_usage_threshold": self.TotalCpuUsageThreshold,
            "single_cpu_usage_threshold": self.SingleCpuUsageThreshold,
        }


class MemoryAlarmRules(models.Model):

    Name = models.CharField(max_length=40, verbose_name="内存报警规则名称")
    MemoryAlarmLevel = models.IntegerField(choices=ALARM_LEVEL, verbose_name="内存报警级别")
    MemoryAlarmTitle = models.CharField(max_length=40, verbose_name="内存报警标题")
    MemoryUsageThreshold = models.IntegerField(verbose_name="内存报警阈值")
    Ip = models.CharField(max_length=16, null=True, unique=True, verbose_name="ip地址")
    Cdn = models.CharField(max_length=24, null=True, verbose_name="cdn")
    ChannelGroup = models.CharField(max_length=24, null=True, verbose_name="频道组")

    class Meta:
        db_table = "memory_alarm_rules"
        verbose_name = "内存报警规则"

    def save(self, *args, **kwargs):
        cache.delete("memory_alarm_rules_" + self.Ip)
        super(MemoryAlarmRules, self).save(*args, **kwargs)

    @property
    def dict_data(self):
        return {
            "name": self.Name,
            "memory_alarm_level": self.MemoryAlarmLevel,
            "memory_alarm_title": self.MemoryAlarmTitle,
            "memory_usage_threshold": self.MemoryUsageThreshold,
        }


class DiskAlarmRules(models.Model):

    Name = models.CharField(max_length=40, verbose_name="硬盘报警级别")
    DiskAlarmLevel = models.IntegerField(choices=ALARM_LEVEL, verbose_name="硬盘报警级别")
    DiskAlarmTitle = models.CharField(max_length=40, verbose_name="硬盘报警标题")
    DiskUsageThreshold = models.IntegerField(verbose_name="硬盘报警阈值")
    Ip = models.CharField(max_length=16, null=True, unique=True, verbose_name="ip地址")
    Cdn = models.CharField(max_length=24, null=True, verbose_name="cdn")
    ChannelGroup = models.CharField(max_length=24, null=True, verbose_name="频道组")

    class Meta:
        db_table = "disk_alarm_rules"
        verbose_name = "cpu报警规则"

    @property
    def dict_data(self):
        return {
            "name": self.Name,
            "disk_alarm_level": self.DiskAlarmLevel,
            "disk_alarm_title": self.DiskAlarmTitle,
            "disk_usage_threshold": self.DiskUsageThreshold,
        }


class DeltaAlarmRules(models.Model):

    Name = models.CharField(max_length=40, verbose_name="延迟报警级别")
    SwitchDelta = models.BooleanField(default=1, choices=Switch, verbose_name="频道延迟异常报警开关")
    DeltaAlarmTitle = models.CharField(max_length=40, verbose_name="频道延迟异常报警标题")
    DeltaMinThreshold = models.IntegerField(verbose_name="频道Delta延迟正常区间的最小值")
    Ip = models.CharField(max_length=16, null=True, unique=True, verbose_name="ip地址")
    Cdn = models.CharField(max_length=24, null=True, verbose_name="cdn")
    ChannelGroup = models.CharField(max_length=24, null=True, verbose_name="频道组")

    class Meta:
        db_table = "delta_alarm_rules"
        verbose_name = "延迟报警规则"

    @property
    def dict_data(self):
        return {
            "name": self.Name,
            "switch_delta": self.SwitchDelta,
            "delta_alarm_title": self.DeltaAlarmTitle,
            "delta_min_threshold": self.DeltaMinThreshold,
        }


class ProcessRules(models.Model):

    Name = models.CharField(max_length=40, verbose_name="进程名称")
    Switch = models.BooleanField(default=1, choices=Switch, verbose_name="开关")
    Type = models.IntegerField(verbose_name="类型")
    Detail = models.CharField(max_length=40, verbose_name="详情")
    Ip = models.CharField(max_length=16, null=True, unique=True, verbose_name="ip地址")
    Cdn = models.CharField(max_length=24, verbose_name="cdn")
    ChannelGroup = models.CharField(max_length=24, null=True, verbose_name="频道组")

    class Meta:
        db_table = "process_rules"
        verbose_name = "cdn进程报警规则"


class Host(models.Model):
    Hostname = models.CharField(max_length=40, verbose_name="主机名")
    MacAddress = models.CharField(max_length=24, verbose_name="mac地址")
    ExternalIp = models.CharField(max_length=16, unique=True, verbose_name="外网ip", default='')
    InternalIp = models.CharField(max_length=16, verbose_name="内网ip", default='')
    OsType = models.CharField(max_length=16, verbose_name="操作系统类型")
    OsVersion = models.CharField(max_length=64, verbose_name="操作系统版本")
    CreateTime = models.DateTimeField(default=datetime.datetime.now(), verbose_name="创建时间")
    UpdateTime = models.DateTimeField(default=datetime.datetime.now(), verbose_name="更新时间")
    Cdn = models.CharField(blank=True, max_length=24, verbose_name="cdn")
    ChannelGroup = models.CharField(blank=True, max_length=24, verbose_name="频道组")

    class Meta:
        db_table = "host"
        verbose_name = "节点详情"
    
    def save(self, *args, **kwargs):
        cache.delete("inner_exter_mapping")
        super(Host, self).save(*args, **kwargs)
        
    @property
    def inter_exter_dict(self):
        return {
            "external_ip": self.ExternalIp,
            "internal_ip": self.InternalIp
        }


class MailSetting(models.Model):
    MailServer = models.CharField(max_length=255, verbose_name="邮件服务地址")
    MailUserName = models.CharField(max_length=24, verbose_name="邮件用户名")
    MailPassword = models.CharField(max_length=40, verbose_name="邮件密码")
    MailRecipients = models.CharField(max_length=255, verbose_name="邮件收件人")
    Cdn = models.CharField(max_length=24, null=True, unique=True, verbose_name="cdn")
    ChannelGroup = models.CharField(max_length=24, null=True, verbose_name="频道组")

    class Meta:
        db_table = "mail_setting"
        verbose_name = "邮件设置"


class WechatSetting(models.Model):
    QyId = models.CharField(unique=True, max_length=24, verbose_name="企业ID")
    AgentId = models.IntegerField(unique=True, verbose_name="应用的AgentId")
    Secret = models.CharField(max_length=64, verbose_name="应用对应的Secret")
    TitleKey = models.CharField(max_length=64, verbose_name="标题中包含的关键字")
    Cdn = models.CharField(max_length=24, null=True, unique=True, verbose_name="cdn")
    ChannelGroup = models.CharField(max_length=24, null=True, verbose_name="频道组")

    class Meta:
        db_table = "wechat_setting"
        verbose_name = "微信设置"

