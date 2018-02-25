#!/usr/bin/env python3

sex=input("请输入你的性别：")

if sex == "男":
    bai = input("你的她白吗：")
    money = int(input("你的她有钱吗："))
    betifull = input("你的她美丽吗：")
    if bai == "白" and money >= 10000 and betifull == "美":
        print("你的她是白富美。。。")
    else:
        print("你的她就是一个普通女孩。。。")
else:
    hight = input("你的他高吗：")
    money = int(input("你的他有钱吗："))
    betifull = input("你的他帅吗：")
    if hight == "高" and money >= 10000 and betifull == "帅":
        print("你的她是高富帅。。。")
    else:
        print("你的他就是一个普通男孩。。。")

