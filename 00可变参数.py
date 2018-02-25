#!/usr/bin/env python3

def sum_nums(a,b,*args):
    print(a)
    print(b)
    print(args)
    #result = a+b+args
    result = 0
    for i in args:
        result+=i
    print(a+b+result)
sum_nums(11,22,33,44,55,66,77)
sum_nums(11,22,33)
