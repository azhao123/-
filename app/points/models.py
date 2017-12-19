# -*- coding: utf-8 -*-

from django.db import models
from users.models import *
from datetime import datetime


class Point(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)
    admin = models.CharField(verbose_name=u"操作人员", max_length=20)
    reason = models.CharField(verbose_name=u"修改理由", max_length=200)
    end_point = models.CharField(verbose_name=u"最后积分", max_length=20)
    var_point = models.CharField(verbose_name=u"增减积分", max_length=20)


    class Meta:
        verbose_name = u"积分表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.wechat_name

