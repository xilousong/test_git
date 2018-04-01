#!/usr/bin/env python3
#encoding: utf-8

art=[2, 4, 5, 9, 12, 17, 23, 30, 55, 67, 89, 99, 122, 123, 235, 355, 666, 2000, 3781, 4567, 5432, 11111, 22222]

start = 0
end  = len(art)-1
input_num = int(input('请输入你要查找的数字：'))

while True:
    mid = (start + end)//2
    mid_num=art[mid]
    
    if input_num not in art:
        print('您输入的数字不在查找的范围。。')
        break
    else:
        if input_num < mid_num:
            end = mid
        elif input_num > mid_num:
            start = mid
        else:
            print("您输入的数字的索引是:{}".format(mid))
            break
   
