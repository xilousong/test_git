#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arr = [1,3,7,10,22,100,299,1000,2000,30000,40000]
print("""请从下面的列表%s中随机输入一个数字,将会
 输出该数字在列表中的索引"""%(arr))
try:
    num = input("请从给定的列表中输入一个数字：")

    for index in range(len(arr)):
        if arr[index] == int(num):
            print(index)
except:
    exit

