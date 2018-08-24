# -*- coding:utf-8 -*-
import json
from django.shortcuts import render
from django.template import loader
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
import hashlib
from Crawl import models

def hashStr(strInfo):
    """
    对字符串进行hash,得到一个16进制的指纹数据
    """
    h = hashlib.md5()
    h.update(strInfo.encode("utf-8"))
    return h.hexdigest()

# Create your views here.


# 登录
def login_views(request):
  if request.method == 'GET':
    # if 'id' in request.session and 'uphone' in request.session:
    #   # 服务器有访问记录,允许免登录,进入主页
    #   return HttpResponseRedirect('/oneindex/')
    # else:
      if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
        # 浏览器中有访问记录,允许免登录,进入主页
        request.session['id'] = request.COOKIES['id']
        request.session['uphone'] = request.COOKIES['uphone']
        return HttpResponseRedirect('/oneindex/')
      else:
        forms = LoginForm()
        return render(request, 'login.html', locals())

  else:
    uphone = request.POST['uphone']
    upwd = request.POST['upwd']
    upwd = hashStr(hashStr(upwd))
    Ulist = Users.objects.filter(uphone=uphone, upwd=upwd)
    if Ulist:
      resp = HttpResponseRedirect('/oneindex/')
      request.session['id'] = Ulist[0].id
      request.session['uphone'] = uphone
      # 设置浏览器关闭则清除服务器上对应的session空间
      SESSION_EXPIRE_AT_BROWSER_CLOSE = True
      if 'isSave' in request.POST:
        resp.set_cookie('id', Ulist[0].id, 60*60)
        resp.set_cookie('uphone', uphone, 60*60)
      return resp
    else:
      forms = LoginForm()
      msg='用户名或密码不正确'
      return render(request, 'login.html', locals())


# 注册
def register_views(request):
  if request.method == 'GET':
    return render(request, 'register.html')
  else:
    uphone = request.POST['uphone']
    upwd = request.POST['upwd']
    upwd = hashStr(hashStr(upwd))
    uList = Users.objects.filter(uphone=uphone)
    if uList:
      return render(request, 'register.html', {'msg': '用户名已经存在'})
    dits = {'uphone': uphone,
            'upwd': upwd}
    Users(**dits).save()
    return HttpResponseRedirect('/login/')


# Ajax 手机号异步查重
def checkphone_views(request):
  uphone = request.POST['uphone']
  uList = Users.objects.filter(uphone=uphone)
  if uList:
    s = 1
    msg ='用户名已经存在'
  else:
    s = 0
    msg = '通过'
  dits = {'status':s,'msg':msg}
  return HttpResponse(json.dumps(dits))


# 退出登录
def quit_views(request):
  rep = HttpResponseRedirect('/index/')
  try:
    rep.delete_cookie('id')
    rep.delete_cookie('uphone')
    del request.session['id']
    del request.session['uphone']
    return rep
  except:
    return rep


# 主页
def index_views(request):
  return render(request, 'index.html')


# 个人主页
def one_index_views(request):
   if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
     # 1.获取用户id和账号
     uphone = request.COOKIES['uphone']
     id = request.COOKIES['id']

     # 2.根据用户id,查找数据库位置信息表,加载出最新的位置信息
     try:
       patterns = Adress.objects.filter(user_id=id)
       num = len(patterns)-1
       adress=patterns[num].adress
       adressid = patterns[num].id
       # 3.根据用户id和位置信息id,查找生活信息表和医疗信息表
       infos_life = models.life_Services.objects.filter(useId=id,positionsId=adressid)
       info_med = models.medical.objects.filter(useId=id,positionsId=adressid)
     except Exception as e:
       print(e)
       adress = '没有位置记录'

     return render(request, 'one_index.html',locals())

   else:
     return HttpResponseRedirect('/index/')


