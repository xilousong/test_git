#!/usr/bin/env python3
# -*- coding: utf-8 -*-

money = 10000
year = 0

while money < 20000:
    money += money*0.0325
    year +=1
    
print("存了 %s 年后，存款为 %.3f。" %(year,money))

