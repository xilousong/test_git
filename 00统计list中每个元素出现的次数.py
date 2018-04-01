#!/usr/bin/env python3
#encoding: utf-8

languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python', 'matlab', 'python', 'go', 'java']

new={}

for i in languages:
    if i not in new:
        new[i]=1
    else:
        new[i]+=1

print(new)
