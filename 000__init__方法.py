#!/usr/bin/env python3

class Cat():
    """定义一个Cat类""" 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    #方法
    def eat(self):
        print("猫在吃鱼.....")
    
    def drink(self):
        print("猫正在喝水......")
    def introduce(self):
        print(self.name)
        print(self.age)
        


# 创建一个对象
tom = Cat("tom",40)

# 调用方法
tom.eat()
tom.drink()

# 给tom对象定义两个属性
#tom.name = "汤姆"
#tom.age = 40

# 获取属性的第一种方式
#print(tom.name)
#print(tom.age)

# 获取属性的第二种方法
tom.introduce()


lanmao = Cat("lanmao",10)
#lanmao.name = "蓝猫"
#lanmao.age = 10

lanmao.introduce()
