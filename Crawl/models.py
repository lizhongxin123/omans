# -*- coding:utf-8 -*-
from django.db import models
# Create your models here.

# 3.用户搜索的商家信息-生活服务
class life_Services(models.Model):
  useId = models.CharField(max_length=5,verbose_name='用户ID')
  positionsId = models.CharField(max_length=5,verbose_name='地址ID')
  firstLevel = models.CharField(max_length=20,verbose_name='一级目录')
  secondLevel = models.CharField(max_length=50,verbose_name='二级目录')
  title = models.CharField(max_length=100,verbose_name='商家名称')
  address = models.CharField(max_length=200,verbose_name = '地址')

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'life_Services'
    verbose_name = '生活服务'
    verbose_name_plural = verbose_name


# 4.用户搜索的商家信息-医疗
class medical(models.Model):
  useId = models.CharField(max_length=5,verbose_name='用户ID')
  positionsId = models.CharField(max_length=5,verbose_name='地址ID')
  firstLevel = models.CharField(max_length=20,verbose_name='一级目录')
  secondLevel = models.CharField(max_length=50,verbose_name='二级目录')
  title = models.CharField(max_length=100,verbose_name='商家名称')
  address = models.CharField(max_length=200,verbose_name = '地址')

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'medical'
    verbose_name = '医疗'
    verbose_name_plural = verbose_name