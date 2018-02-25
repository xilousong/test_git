#!/usr/bin/env python3

message1=""" 请输入您想要计算的图形(1/2)：
            1、正方形
            2、立方体 """

message2=""" 请输入您想要计算的内容(1/2)：
            1、面积
            2、体积 """

mj=0
tj=0

def jisuan():
    try:
        print(message1)
        ch1=int(input('> '))
        bc=float(input("请输入边长: "))
        
        if ch1 == 1:
            mj = bc ** 2 
            return '正方形的面积为 '+ str(mj) 
        else:
            print(message2)
            ch2=int(input('> '))
            if ch2 == 1:
                mj = (bc ** 2) * 6
                return "立方体的面积为 " + str(mj)
            else:
                tj = bc ** 3
                return "立方体的体积为 " + str(tj)
    
    except KeyboardInterrupt as e:
        return e

print(jisuan())
