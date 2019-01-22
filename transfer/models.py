from __future__ import unicode_literals

from django.db import models


class ServerRules(models.Model):
    ALARM_LEVEL = (
        (1, "邮件报警"),
        (2, "邮件加微信报警"),
        (3, "待定")
    )
    Cdn = models.CharField(max_length=24, primary_key=True, verbose_name="cdn")
    ChannelGroup = models.CharField(max_length=24, verbose_name="频道组")
    CpuAlarmLevel = models.IntegerField(choices=ALARM_LEVEL, verbose_name="cpu报警级别")
    CpuAlarmTitle = models.CharField(max_length=40, verbose_name="cpu报警标题")
    TotalCpuUsageThreshold = models.IntegerField(verbose_name="总cpu报警阈值")
    SingleCpuUsageThreshold = models.IntegerField(verbose_name="单个cpu报警阈值")
    MemoryAlarmLevel = models.IntegerField(choices=ALARM_LEVEL, verbose_name="内存报警级别")
    MemoryAlarmTitle = models.CharField(max_length=40, verbose_name="内存报警标题")
    MemoryUsageThreshold = models.IntegerField(verbose_name="内存报警阈值")
    DiskAlarmLevel = models.IntegerField(choices=ALARM_LEVEL, verbose_name="硬盘报警级别")
    DiskAlarmTitle = models.CharField(max_length=40, verbose_name="硬盘报警标题")
    DiskUsageThreshold = models.IntegerField(verbose_name="硬盘报警阈值")

    SwithDelta = models.BooleanField(default=1, verbose_name="频道延迟异常报警开关")
    DeltaAlarmTitle = models.CharField(max_length=40, verbose_name="频道延迟异常报警标题")
    DeltaMinThreshold = models.IntegerField(verbose_name="频道Delta延迟正常区间的最小值")

    SwithRsServer = models.BooleanField(default=1, verbose_name="Room Server检测开关")
    RsAlarmTitle = models.CharField(max_length=40, verbose_name="rs异常报警标题")

    class Meta:
        db_table = "server_rules"
        verbose_name = "服务端全局配置"


class IpRules(models.Model):
    Ip = models.CharField(max_length=16, verbose_name="ip地址")
    TotalCpuUsageThreshold = models.IntegerField(verbose_name="总cpu报警阈值")
    SingleCpuUsageThreshold = models.IntegerField(verbose_name="单个cpu报警阈值")
    MemoryUsageThreshold = models.IntegerField(verbose_name="内存报警阈值")
    DiskUsageThreshold = models.IntegerField(verbose_name="硬盘报警阈值")
    Cdn = models.ForeignKey(ServerRules, on_delete=models.CASCADE, verbose_name="cdn")

    class Meta:
        db_table = "ip_rules"
        verbose_name = "节点基础配置"


class RoomServerUrl(models.Model):
    Cdn = models.ForeignKey(ServerRules, on_delete=models.CASCADE, verbose_name="cdn")
    RsServerUrl = models.CharField(max_length=40, verbose_name="rs url地址")

    class Meta:
        db_table = "room_server_url"
        verbose_name = "rs服务地址"


class Host(models.Model):
    Hostname = models.CharField(max_length=40, verbose_name="主机名")
    MacAddress = models.CharField(max_length=24, verbose_name="mac地址")
    ExternalIp = models.CharField(max_length=16, verbose_name="外网ip", default='')
    InternalIp = models.CharField(max_length=16, verbose_name="内网ip", default='')
    OsType = models.CharField(max_length=16, verbose_name="操作系统类型")
    OsVersion = models.CharField(max_length=64, verbose_name="操作系统版本")
    Cdn = models.ForeignKey(ServerRules, default=None, on_delete=models.CASCADE, verbose_name="cdn")

    class Meta:
        db_table = "host"
        verbose_name = "节点详情"


class MailSetting(models.Model):
    MailServer = models.CharField(max_length=255, verbose_name="邮件服务地址")
    MailUserName = models.CharField(max_length=24, verbose_name="邮件用户名")
    MailPassword = models.CharField(max_length=40, verbose_name="邮件密码")
    MailRecipients = models.CharField(max_length=255, verbose_name="邮件收件人")
    Cdn = models.ForeignKey(ServerRules, on_delete=models.CASCADE, verbose_name="cdn")

    class Meta:
        db_table = "mail_setting"
        verbose_name = "邮件设置"


class WechatSetting(models.Model):
    QyId = models.CharField(max_length=24, verbose_name="企业ID")
    AgentId = models.IntegerField(verbose_name="应用的AgentId")
    Secret = models.CharField(max_length=64, verbose_name="应用对应的Secret")
    TitleKey = models.CharField(max_length=64, verbose_name="标题中包含的关键字")
    Cdn = models.ForeignKey(ServerRules, on_delete=models.CASCADE, verbose_name="cdn")

    class Meta:
        db_table = "wechat_setting"
        verbose_name = "微信设置"

