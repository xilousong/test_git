#!/usr/bin/env python3


class Name():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def set_name(self,new_name):
        self.__name = new_name

    def set_age(self,new_age):
        if new_age >0 and new_age <100:
            self.__age = new_age
        else:
            self.__age = 0

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age



    def __str__(self):
        return "我叫%s,今年%d 岁"%(self.get_name(),self.get_age())

p = Name("小明",20)

print(p)

p.set_name("明明")
print(p)

p.set_age(30)
print(p)


p.set_age(300)
print(p)
