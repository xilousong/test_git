#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','css','html']
d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
