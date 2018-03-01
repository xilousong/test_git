#!/usr/bin/env python3
#-*- coding: utf-8 -*-

arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,14,21,14]
arr_common = []

for i in arr2:
    if i not in arr_common and i in arr1:
        arr_common.append(i) 

print(arr_common)
