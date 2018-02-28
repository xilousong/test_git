#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arr = [45,67,122,65,89,44,66,12,5,90,4,13,19,2,6,84,47]

#计算出列表元素个数
arr_lenth = len(arr)
#记录执行了多少此循环
count = 0
#列表中有多少个元素就循多少次
while arr_lenth:
    #采用range函数生成一个序列，比列表实际元素少一位数字，因为如果
    #刚好实用序列的个数，当下面比较时“arr[i+1]”会超出列表范围
    for i in range(arr_lenth-1):
        #每循环一次count加一
        count +=1
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        #打印每次冒泡排序后的结果
        print(arr)
    #每完成一次冒泡，arr_lenth 减一，当列表中所有元素都完成冒泡循环结束
    arr_lenth-=1        
#打印冒泡完成后的列表
print(arr)
#打印循环总次数
print(count)
