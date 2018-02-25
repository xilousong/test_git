#!/usr/bin/env python3

#定义一个全局变量names,用来存储名片信息
names = {}

def tishi():
    """打印提示信息"""
    mess="""
	      名片管理系统 V1.0
	      1、显示所以名片
	      2、添加名片
	      3、修改名片
	      4、删除名片
	      5、查询名片
	      6、保存信息
	      7、退出系统
	"""
    print(mess)

def find_all():
    """打印所有的名片"""
    global names
    print("姓名\t年龄\t手机\t地址")
    for i in names.keys():
        print("%s\t%s\t%s\t%-10s"%(i,names[i]['age'],names[i]['phone'],names[i]['addr']))

def add_name():
    """添加新的名片"""
    global names
    name = input("请输入您想要添加的姓名：")
    age = input("请输入年龄：")
    phone = input("请输入手机号码：")
    addr = input("请输入地址：")
    person = {}
    person["age"] = age
    person["phone"] = phone
    person["addr"] = addr
    names[name] = person
    
def change_name():
    """修改指定的名片"""
    global names
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
    
def del_name():
    """删除指定的名片"""
    global names
    name = input("请输入您想要删除的姓名： ")
    if name not in names.keys():
        print("输入有误，查无此人！！！")
    else:
        del names[name]

def find_name():
    """查找指定的名片"""
    global names
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


def save_2_file():
    """把已经添加的信息保存到文件中"""
    f = open("backup.data", "w")
    f.write(str(names))
    f.close()

def load_info():
    global names
    try:
        f = open("backup.data")
        names = eval(f.read())
        f.close()
    except Exception:
        pass
    
def main():
	"""完成整个程序的控制"""
	tishi()
	try:
		# 加载之前的数据到程序中
		load_info()

		while True:
		    choice = int(input("请输入您的操作： "))
		    if choice == 1:
		        find_all()
		    elif choice == 2:
		        add_name()
		    elif choice == 3:
		        change_name()
		    
		    elif choice == 4:
		        del_name()

		    elif choice == 5:
		        find_name()

		    elif choice == 6:
		        save_2_file()

		    elif choice == 7:
		        break
		    else: 
		        print("您的输入有误，请按照提示进行输入.......")
		print()

	except (KeyboardInterrupt,ValueError) as a:
		print(a)

if __name__ == "__main__":
    #调用主函数
    main()
