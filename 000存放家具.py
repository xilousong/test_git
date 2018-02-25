#!/usr/bin/env python3

# 定义一个家 的类
class Home():
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []

    def __str__(self):
        return """房子的总面积是:%s,可用面积是:%s,房子的户型是:%s,地址是:%s,现在房子里面有:%s"""%(self.area,self.left_area,self.info,self.addr,str(self.contain_items))

    # 定义一个添加家具的方法
    def add_items(self,item):
        self.contain_items.append(item.get_name())
        self.left_area -= item.get_area()

# 定义一个床的类
class Bed():
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "%s占用的面积是：%d"%(self.name,self.area)

    # 获取对象的名字
    def get_name(self):
        return self.name
    # 过去对象的面积
    def get_area(self):
        return self.area

# 创建一个家的对象 fangzi
fangzi = Home(120,"三房一厅","长沙市，芙蓉区")
print(fangzi)

# 创建一个床的对象 chuang

chuang = Bed("电脑桌",2)
print(chuang)

fangzi.add_items(chuang)
print(fangzi)
chuang = Bed("双人床",4)
print(chuang)
fangzi.add_items(chuang)
print(fangzi)
chuang = Bed("席梦思",6)
print(chuang)
fangzi.add_items(chuang)
print(fangzi)
chuang = Bed("沙发",10)
print(chuang)
fangzi.add_items(chuang)
print(fangzi)
chuang = Bed("茶几",8)
print(chuang)
fangzi.add_items(chuang)
print(fangzi)
