#!/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:李仲新 time:2018/8/13
import random
from urllib import request,error
import logging

# 1.日志创建
import io
import sys
import time

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s ')
file_handler = logging.FileHandler('CrawlHtml.log')
file_handler.setFormatter(formatter)
logger = logging.getLogger('CrawlHtml')
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

# 2.UA池
UA_list = [
  ('User-Agent','Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'),
  ('User-Agent','Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'),
  ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"),

]
# 4.主函数
def downloadHtml(url,headers=[],proxy={},timeout=3,times_calback=0,decodeInfo='utf-8'):
  # 4.1 初始化输出值
  html = ''

  # 4.2 递归出口
  if times_calback > 3:
    logger.error('request urlopen error:4.2')
    return html

  # 4.3 添加UA
  headers.append(random.choice(UA_list))
  # print(headers)

  # 4.4 加载代理服务器
  if random.randint(1,10) < 5:
    proxy = {}

  proxy_handler = request.ProxyHandler(proxy)
  opener = request.build_opener(proxy_handler)
  opener.addheaders = headers
  request.install_opener(opener)

  # 4.5 访问网页
  try:
    response = request.urlopen(url, timeout=5)  # urlopen没事设置headers的功能
    html = response.read().decode(decodeInfo)
    logger.info('request urlopen ok')
  except UnicodeDecodeError as e:
    logger.error('编码异常: ' + e)
  except error.HTTPError or error.URLError as e:
    logger.error('urllib error: ' + e)
    if hasattr(e, 'code') and 400 <= e.code < 500:  # 客户端问题，通过分析日志来跟踪
      logger.error("Client Error")
    elif hasattr(e, 'code') and 500 <= e.code < 600:  # 服务器问题,再次尝试访问
      html = downloadHtml(url, headers, proxy, timeout,  times_calback+1,decodeInfo )  # 再次尝试访问
      time.sleep(random.randint(1, 3))  # 休息的时间可以自己定义一个策略
  except Exception as e:
    logger.error(e)

  return html


if __name__ == '__main__':
  url = 'http://www.sina.com.cn'
  html = downloadHtml(url)

  sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
  print(html)

  logger.removeFilter(file_handler)