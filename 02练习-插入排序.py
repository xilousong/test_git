#!/usr/bin/env python3
#encoding: utf-8

art=[]

while True:
    lenth = len(art)
    input_num = input("请输入一个数字或(q): ")
    if input_num == "q":
        print(art)
        break
    else:
        art.append(int(input_num))
        lenth = len(art)
        if lenth > 1:
            end = lenth -1
        else:
            end = 0
        while end > 0:
            if  art[end] < art[end-1]:
                art[end],art[end-1] = art[end-1],art[end]
            end -= 1

