#!/usr/bin/env python3

class Cat():
    """定义一个Cat类""" 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return "%s的年龄是：%d"%(self.name,self.age) 


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

lanmao = Cat("lanmao",10)

print(tom)
print(lanmao)
