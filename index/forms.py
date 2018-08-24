#!/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:李仲新 time:2018/8/15
from .models import *
from django import forms


class LoginForm(forms.ModelForm):
  class Meta:
    model = Users
    fields = ['uphone','upwd']
    labels = {
        'uphone':'账号',
        'upwd':'密码',
    }
    widgets = {
        'uphone':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'请输入手机号',
                'name':'uphone',
            }
        ),
        'upwd':forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'请输入密码',
                'name':'upwd',
            }
        ),
    }


