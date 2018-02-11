#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
    year = int(input("please input a year: "))
    if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
        print("%s 年是闰年。" % (year))
        break
    else:
        print("%s 年不是闰年。" % (year))
    

