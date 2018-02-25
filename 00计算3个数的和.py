#!/usr/bin/env python3

def jisuan(a,b,c):
    return a+b+c

def avrege(a,b,c):
    result = jisuan(a,b,c)
    return result/3

def pingfang(a,b,c):
    result = avrege(a,b,c)
    return result**2
    

num1=int(input("请输入一个数字："))
num2=int(input("请输入二个数字："))
num3=int(input("请输入一个数字："))

#print("%d+%d+%d=%d"%(num1,num2,num3,jisuan(num1,num2,num3)))
print(pingfang(num1,num2,num3))
