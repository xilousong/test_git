#!/usr/bin/env python3

mess="""
      名片管理系统 V1.0
      1、显示所以名片
      2、添加名片
      3、修改名片
      4、删除名片
      5、查询名片
      6、退出系统
"""
print(mess)

names = {}

try:

	while True:
		choice = int(input("请输入您的操作： "))

		if choice == 1:
		    print("姓名\t年龄\t手机\t地址")
		    for i in names.keys():
		        print("%s\t%s\t%-11s\t%-10s"%(i,names[i]['age'],names[i]['phone'],names[i]['addr']))

		elif choice == 2:
		    name = input("请输入您想要添加的姓名：")
		    age = input("请输入年龄：")
		    phone = input("请输入手机号码：")
		    addr = input("请输入地址：")
		    person = {}
		    person["age"] = age
		    person["phone"] = phone
		    person["addr"] = addr
		    names[name] = person
		    
		elif choice == 3:
		    name = input("请输入您想要修改的姓名：")
		    if name not in names.keys():
		        print("查无此人！！！")
		    else:
		        content = input("请输入您想要修改的内容(age/addr/phone): ")
		        if content not in names[name].keys():
		            print("无此选项，请输入正确的内容。。。")
		        else:
		            new_content = input("请输入您修改后的内容：")
		            names[name][content] = new_content
		    
		elif choice == 4:
		    name = input("请输入您想要删除的姓名： ")
		    if name not in names.keys():
		        print("输入有误，查无此人！！！")
		    else:
		        del names[name]
		
		elif choice == 5:
		    name = input("请输入您要查找的姓名：")
		    if name not in names.keys():
		        print("查无此人！！！")
		    else:
		        print(
"""=================
姓名：%s
年龄：%s
手机：%s
地址：%s
=================
"""%(name,names[name]["age"],names[name]["phone"],names[name]["addr"]) )

		elif choice == 6:
		    break

		else: 
		    print("您的输入有误，请按照提示进行输入.......")
		print()
except (KeyboardInterrupt,ValueError) as a:
	print(a)
