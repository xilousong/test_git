#!/usr/bin/env python3

import random 

computer = random.randint(0,2)

player = int(input("请输入 0石头 1剪刀 2布：\n"))

if (player == 0 and computer ==1) or (player == 1 and computer == 2) or (player ==2 and computer == 0):
    print("恭喜你，你赢了。。。")
elif player == computer:
    print("平局。。。")
else:
    print("你输了。。。。")


