#!/usr/bin/env python3
#-*- coding: utf-8 -*-

arr = [1,2,3,4,2,12,3,14,3,14,3,21,2,2,3,4111,22,3333,4]
arr_new = []

for i in range(len(arr)):
    if arr[i] not in arr_new:
        arr_new.append(arr[i])
#打印去重后的新的列表
print(arr_new)
