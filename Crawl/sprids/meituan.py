#!/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:李仲新 time:2018/8/17
import csv
import json
import re
import urllib
from .mybasicSpider import *
from lxml import etree
from ..models import *


# 4.保存数据
def save_content(content, useId, positionsId):
    i = 0
    for goods in content:
      i+=1
      if i >= 50:
        break
      if goods[0] == '生活服务':
        dic = {
          'useId':useId,
          'positionsId':positionsId,
          'firstLevel':goods[0],
          'secondLevel':goods[1],
          'title':goods[2],
          'address':goods[3],
        }
        life_Services(**dic).save()
      elif goods[0] == '医疗':
        dic = {
          'useId':useId,
          'positionsId':positionsId,
          'firstLevel':goods[0],
          'secondLevel':goods[1],
          'title':goods[2],
          'address':goods[3],
          }
        medical(**dic).save()


# 3.提取商家信息
def filter_content(careID,key):
  for id in careID:
    # 判断是不是一级目标
    if type(id[0]) == type('str'):
      types = id[1]  # 保存一级目录
      continue
    for i in range(1):
      url = 'http://apimobile.meituan.com/group/v4/poi/pcsearch/50?uuid=0fbf99feb5a04e9b9f55.1534727932.1.0.0&userid=-1&limit=32&offset={}&cateId={}&q={}'.format(i*32,id[0],key)
      print(url)
      html = get_html(url)
      date = json.loads(html)
      result = date['data']["searchResult"]
      if result:
        # print(result)
        for item in result:
           yield [types,id[1],item['title'], item['address'], item['avgscore']] #一级目录 二级目录 商家名称 地址 评分

#    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


# 2.提取careID
def filter_ID(html):
  careID = []
  root = etree.HTML(html)
#  sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
  try:
    script = root.xpath('//*[@id="main"]/script[3]/text()')[0]
    reg_care = '"category":([\s\S]*?),"data"'
    reg_object_care = re.compile(reg_care)
    care = re.findall(reg_object_care, script)[0]
    care_json = json.loads(care)
    for items in care_json['children']:
        #  一级大类
        if items['name'] == '生活服务' or items['name'] == '医疗':
          careID.append((str(items['id']), items['name']))
          for children in items['children']:
            careID.append((children['id'], children['name']))
    return careID
  except:
    return careID


# 1.获取html
def get_html(url):
  headers = [("Cookie", '__mta=46412440.1534504833274.1534728331047.1534728551560.7;__mta=46412440.1534504833274.1534565788638.1534567641481.5;')]
  html = downloadHtml(url, headers=headers)
  return html


# 主函数
def main(key, useId, positionsId):  # 位置 用户id 位置信息id
  print('美团网数据抓取')
  # 1.获取首页html
  dit = {key: ''}
  key = urllib.parse.urlencode(dit)[:-1:]
  url = 'http://hz.meituan.com/s/{}'.format(key)
  html = get_html(url)

  # 2.提取商品信息careID(生活服务/医疗)
  careID = filter_ID(html)

  # 3.提取提取商家信息
  content = filter_content(careID, key)

  # # 4.保存内容
  save_content(content, useId, positionsId)

  # 反馈是否有爬取到数据
  if careID:
    return 1
  else:
    return 0

if __name__ == '__main__':
  key = input('请输入查询内容:')
  main(key)