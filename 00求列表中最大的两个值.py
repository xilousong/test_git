#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_num1 = 0
max_num2 = 0

for i in l:
    for j in l:
        if j > max_num1:
           max_num1 = j
    if i > max_num2 and i < max_num1:
        max_num2 = i

print("最大的两个值分别是：%s，%s" %(max_num1,max_num2))    
