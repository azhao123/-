# -*- coding: utf-8 -*-
from django.db import models
from products.models import *
from users.models import *
from django.conf import settings

class Orders(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    product = models.OneToOneField(Product)
    add_time = models.DateTimeField(verbose_name=u"下单时间", default=datetime.now)
    sure_tiem = models.DateTimeField(verbose_name=u"确认收货时间")
    send_time = models.DateTimeField(verbose_name=u"发货时间")
    send_company = models.CharField(verbose_name=u"物流公司", max_length=20)
    send_code = models.CharField(verbose_name=u"快递单号", max_length=20)
    
    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name
    
    def __unicode__(self):
        return self.user.wechat_name
