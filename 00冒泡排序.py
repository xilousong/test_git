#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arr = [45,67,23,4,13,19,2,6,84,47]

arr_lenth = len(arr)

while arr_lenth:
    for i in range(arr_lenth):
        if i == arr_lenth -1:
            break
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    arr_lenth-=1        
print(arr)
