#!/usr/bin/env python3
# -*- coding:utf-8 -*-

name=input("请输入您的姓名：")
phone=input("请输入您的手机号码：")
addr=input("请输入您的地址：")

print("="*20,end='')
print("""
  姓名:{}
  手机:{}
  地址:{}""".format(name,phone,addr))
print("="*20)
