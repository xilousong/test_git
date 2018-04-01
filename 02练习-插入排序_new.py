#!/usr/bin/env python3
#encoding: utf-8

art=[15]
insert=[1,4,3,2434,6,222,45,8,12,333,777,234,21,34,23,25,43,38,33,70,9,17,28]


while True:
    art.append(insert.pop())
    lenth = len(art)
    end = lenth -1
    while end > 0:
        if  art[end] < art[end-1]:
            art[end],art[end-1] = art[end-1],art[end]
        end -= 1
    if len(insert) == 0:
        print(art)
        break
