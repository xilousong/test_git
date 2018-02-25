#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person(object):
    
    
    def __new__(cls,*args, **kwargs):
        print("new方法，创建对象，分配内存空间。。。。")
        instance = super().__new__(cls)
        
        return instance

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("我的名字叫 %s，今年 %d岁"%(self.name,self.age))

p1 = Person("tom",25)

print(p1)
