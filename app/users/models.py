# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from products.models import Product

class UserProfile(AbstractUser):
    image = models.ImageField(verbose_name=u"头像", upload_to='user/image/%Y/%m/%d', default=u"user/image/default.png", max_length=100)
    sex = models.CharField(choices=(('male', u"男"), ('female', u'女')), default='male', max_length=6)
    points = models.IntegerField(verbose_name=u"积分", default=0)
    mobile = models.CharField(verbose_name=u"手机号码", max_length=50)
    city = models.CharField(verbose_name=u"城市", max_length=20)
    country = models.CharField(verbose_name=u"国家", max_length=20)
    province = models.CharField(verbose_name=u"省份", max_length=20)
    wechat_name = models.CharField(verbose_name=u"微信名", max_length=20)
    Openid = models.CharField(verbose_name='OpenID', max_length=80)

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.wechat_name

class Banner(models.Model):
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=100, verbose_name=u"标题")
    title = models.CharField(max_length=100, verbose_name=u"标题")
    url = models.URLField(max_length=100, verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    index = models.IntegerField(default=100, verbose_name=u"顺序")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class UserFav(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.ForeignKey(Product, verbose_name=u"商品")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

