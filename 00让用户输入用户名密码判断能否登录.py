#!/usr/bin/env python3
#-*- coding: utf-8 -*-

arr= ["user:pwd","user1:pwd1","user2:123"]

User = input("请输入用户名：")
passwd = input("请输入密码：")
str_login = ':'.join([User,passwd])

#for i in arr:
if str_login in arr:
    print("wellcome to login")
else:
    print("login error!!! 用户名或密码不正确！")
