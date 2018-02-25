#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open("/root/python/aaa")
f_copy = open("/root/python/aaa[附件]","w")


while True:
    
    txt = f.readline()
    if not txt:
        break
    
    f_copy.write(txt[::-1])






f.close()
f_copy.close()


