# -*- coding: utf-8 -*-

from django.db import models
from orders.models import *
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"商品名称")
    price = models.IntegerField(verbose_name=u"价格")
    point = models.IntegerField(verbose_name=u"商品积分")
    nicimage = models.ImageField(verbose_name=u"商品缩略图", upload_to= 'product_nic/%Y/%m', max_length=100, default='product_nic/default.png')
    image = models.ImageField(verbose_name=u"商品图片", upload_to='product/%Y/%m', max_length=100, default='product/default.png')
    image2 = models.ImageField(verbose_name=u"商品图片2", upload_to='product/%Y/%m', max_length=100,
                              default='product/default.png')
    image3 = models.ImageField(verbose_name=u"商品图片3", upload_to='product/%Y/%m', max_length=100,
                              default='product/default.png')
    image4 = models.ImageField(verbose_name=u"商品图片4", upload_to='product/%Y/%m', max_length=100,
                              default='product/default.png')
    image5 = models.ImageField(verbose_name=u"商品图片5", upload_to='product/%Y/%m', max_length=100,
                              default='product/default.png')
    des = models.CharField(verbose_name=u"商品详细描述", max_length=500)
    add_time = models.DateTimeField(verbose_name=u"商品上架时间")
    sell_nums = models.IntegerField(verbose_name=u"商品销量")
    ku_cun = models.IntegerField(verbose_name=u"商品库存")
    comment = models.CharField(verbose_name=u"评论", default='', max_length=500)
    tag = models.IntegerField(verbose_name="分类",choices=((1, u'礼品箱包'), (2, u'家居家装'), (3, u'数码办公'), (4, u'服饰鞋帽'), (5, u'家用电器'), (6, u'个护化妆'), (7, u'厨房餐饮'), (8, u'珠宝手表'), (9, u'运动健康')), default=1)
    brand = models.IntegerField(verbose_name="品牌", choices=((1,'addids'), (2, 'lining'), (3, 'baidu')), default=1)
    content = RichTextField(default='')
    content2 = RichTextUploadingField(default='')

    class Meta:
        verbose_name = u"商品"
        verbose_name_plural = verbose_name
        
    def __unicode__(self):
        return self.name



