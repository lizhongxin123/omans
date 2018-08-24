# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.
# 1.用户信息
class Users(models.Model):
  uphone = models.CharField(max_length=11,verbose_name='电话号码')
  upwd = models.CharField(max_length=30,verbose_name='密码')
  iaActiv = models.BooleanField(default=True)

  def __str__(self):
    return self.uphone

  class Meta:
    db_table = 'users'
    verbose_name = '用户表'
    verbose_name_plural = verbose_name


# 2.用户位置信息:与用户信息一对多关系
class Adress(models.Model):
  adress = models.CharField(max_length=30, verbose_name='地址')
  user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='用户')  # user_id

  def __str__(self):
    return self.adress

  class Meta:
    db_table = 'adress'
    verbose_name = '用户位置'
    verbose_name_plural = verbose_name

