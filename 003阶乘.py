#!/usr/bin/env python3

num = int(input("情输入您想计算的阶乘数： "))

def jiecheng(a):
    if a == 1:
        return 1
    else:
        return a*jiecheng(a-1)
        
print(jiecheng(num))
