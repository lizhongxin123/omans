#!/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:李仲新 time:2018/8/20
import csv
from .mybasicSpider import *
import random
import urllib
import re
from bs4 import BeautifulSoup
import time
from ..models import *


# 2.4 保存数据
def save_goods(goods,useId,positionsId):
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


# 2.5 获取商家信息:一级目录(生活服务) 二级目录 商家名称 地址 评分
def get_goods(html):
    try:
      soup = BeautifulSoup(html, 'html.parser')
      # 二级目录
      h_crumbs = soup.find_all('div', class_="h-crumbs")[0].contents[3].contents[7].text
      # 商家名称
      title = soup.find_all('h1', class_="p1")[0].text
      # 地址
      address = soup.find_all('p', class_="fl")[0].contents[-1]
      return ['生活服务',h_crumbs.strip(),title.strip(),address]
    except:
      return ['生活服务','***','***','***']



# 2.3 获取html里的所有商家url
def get_goods_url(html):
  reg = '<dl class="list-sty1-bg clearfix">[\s\S]*?href="([\s\S]*?)"'
  reg_obj = re.compile(reg)
  urls = re.findall(reg_obj,html)
  for url in urls:
    yield 'http://hz.ganji.com'+url


# 2.2 获取html里的所有url
def get_Url(html):
  reg = '<li gjalog[\s\S]*?href="([\S\s]*?)"'
  reg_obj = re.compile(reg)
  pattens = re.findall(reg_obj,html)
  for url in pattens:
    yield 'http://hz.ganji.com'+url


# 2.1获取html页面
def get_html(url):
  html = downloadHtml(url)
  # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
  return html


# 1.主函数
def main(key,useId,positionsId):
# def main(key):
  print('赶集网数据抓取')
  # 二级目录
  Crawl_queue = []
  Crawled_queue = []
  # 店家目录
  Goods_queue = []

  # 1.手动创建一级主目录的url路径,并保存到待爬队列中
  wt = {key: ''}
  key = urllib.parse.urlencode(wt)[:-1]
  url = 'http://hz.ganji.com/huangye/s/_{}'.format(key)
  Crawl_queue.append(url)

  # 2.从二级目录中获取店家的url,同时扩展二级目录
  while Crawl_queue:
    url = Crawl_queue.pop(0)
    Crawled_queue.append(url)
    html = get_html(url)
    # 2.1二级目录扩充
    urls = get_Url(html)
    for url in urls:
      if url not in Crawled_queue:
        Crawl_queue.append(url)
    Crawl_queue = list(set(Crawl_queue))
    # 2.2获取店家url
    goods = get_goods_url(html)
    for url in goods:
      Goods_queue.append(url)


  print(Goods_queue)
  i = 0
  # 3.获取商家详细信息,保存到文件
  for url in Goods_queue:
    i += 1
    print(url)
    html = get_html(url)
    goods = get_goods(html)
    time.sleep(random.randint(1, 3))
    save_goods(goods,useId,positionsId)
    if i > 20:
      break

if __name__ == '__main__':
  key = input("请输入地址:")
  main(key)





