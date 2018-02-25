#!/usr/bin/env python3
#-*- coding: utf-8 -*-

avrage = 0
times = 0
Sum = 0

while not avrage:
    num = input("请输入一个数字： ")
    if num is '':
        if times == 0:
            print("您没有输入任何数字。。。")
        else:
            avrage = Sum/times
            break
    else:
        Sum += int(num)
        times+=1
                
print(avrage)

