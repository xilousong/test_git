#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mess = """
========================
   名字关系系统 V8.6
1、添加一个新名字
2、删除一个名字
3、修改一个名字
4、查询一个名字
q/quit、退出系统
=========================
"""

try:
	names = []

	print(mess)
#		print("   名字关系系统 V8.6")
#		print("1、添加一个新名字")
#		print("2、删除一个名字")
#		print("3、修改一个名字")
#		print("4、查询一个名字")
#		print("q/quit、退出系统")
#		print("="*50)

	while True:

		choice = input("请输入您要进行的操作：\n")

		if choice == "1":
		    add_name = input("请输入您要增加的姓名：")
		    names.append(add_name)
		    print(names)
		    print("%s添加成功....."%add_name)
		elif choice == "2":
		    del_name = input("请输入您要删除的姓名：")
		    names.remove(del_name)
		    print(names)
		    print("%s删除成功....."%del_name)
		elif choice == "3":
		    origin_name = input("请输入您需要修改的姓名：")
		    origin_index = names.index(origin_name)
		    names[origin_index]=input("请输入您修改后的姓名：")
		    print(names)
		    print("%s添加成功....."%names[origin_index])
		elif choice == "4":
                    check_name = input("请输入您想要查询的姓名：")
                    if check_name in names:
                        print("找到了%s"%check_name)
                    else:
                        print("查无此人！！！")
		elif str(choice) == "q" or str(choice) == "quit":
                    break 
		else:
                    print("请输入正确的操作选项。。。",end="\n")
except (KeyboardInterrupt,ValueError) as e:
    print(e)
