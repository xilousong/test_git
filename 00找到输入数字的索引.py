#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arr = [1,3,7,10,22,100,299,1000,2000,30000,40000]

#列表起始位置
start = 0
#列表结束位置
end = len(arr)-1
#要找的数字
num_to_find = int(input("请输入你要查找的数字："))

while True:
    #中间位置索引
    mid = (start+end)//2
    #中间值
    mid_num = arr[mid]
    # 如果找不到，就判断应该在列表的哪个数字(索引)之后
    if mid == start:
        print("can't find ,should after %s==>%s" %(start,arr[start]))
        break
    #如果输入的数字比中间的数字大，则在数组右边
    if num_to_find > mid_num:
        start = mid
    #如果输入的数字比中间的数字小，则在数组左边
    elif num_to_find < mid_num:
        end = mid
    else:
        print("find",mid)
        break
