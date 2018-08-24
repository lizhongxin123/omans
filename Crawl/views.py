# -*- coding:utf-8 -*-
import sys
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Crawl.sprids import ganjiwang, meituan
from index import models

# Create your views here.
# 搜索框
def search_view(request):
  print('search')
  value = request.GET['val']
  useId = request.COOKIES['id']

  # 查询数据库,看是否有重复的位置信息,有重复输入,则直接加载数据库,不需要爬虫爬取数据
  contents = models.Adress.objects.filter(adress=value,user_id=useId)
  if contents:
    return HttpResponse('位置已存在')

  else:
    # 保存位置信息到数据库
    dic = {
      'adress': value,
      'user_id': useId,
    }
    models.Adress(**dic).save()
    pattens = models.Adress.objects.filter(adress=value, user_id=useId)
    print(pattens)
    print(pattens[0].id)
    print(pattens[0].adress)
    print(pattens[0].user_id)

    # 爬取数据
    # ganjiwang.main(pattens[0].adress,pattens[0].user_id,pattens[0].id)
    result = meituan.main(pattens[0].adress, pattens[0].user_id, pattens[0].id)
    # 判断数据是否成功获取
    if result == 1:
      return HttpResponse('获取数据成功')
    else:
      # 删除本条数据库中的位置信息
      models.Adress.objects.get(id=pattens[0].id).delete()
      return HttpResponse('获取数据失败')

