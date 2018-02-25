#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MusicPlayer(object):
    #创建一个类属性，用来保存创建的对象的引用，初始值为None 
    __instance = None

    # 定义一个初始化的属性，初始值为False
    init_flag = False
   
    def __new__(cls):
        if cls.__instance is None:
            #调用父类的__new__方法创建对象
            cls.__instance = super().__new__(cls)
        # 返回对象的引用
        return cls.__instance

    def __init__(self):
        # 判断是否执行过初始化
        if MusicPlayer.init_flag is False:
        # 如果没有执行过初始化，再执行初始化动作
            print("初始化播放器。。。")
            # 修改初始化属性值
            MusicPlayer.init_flag = True

# 创建多个对象，打印每个对象的内存地址
p1 = MusicPlayer()
print(id(p1))
p2 = MusicPlayer()
print(id(p2))
p3 = MusicPlayer()
print(id(p3))
p4 = MusicPlayer()
print(id(p4))
p5 = MusicPlayer()
print(id(p5))
