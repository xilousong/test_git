#!/usr/bin/env python3

class SweetPotato():
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "总共烤了%d 分钟，现在的地瓜是：%s,当中添加的酌料是：%s" %(self.cookedLevel,self.cookedString,str(self.condiments))

    def cook(self,cooked_time):
        
        self.cookedLevel += cooked_time
        
        if self.cookedLevel >=0 and self.cookedLevel <3:
            self.cookedString = "生的"
        elif self.cookedLevel >=3 and self.cookedLevel <5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >=5 and self.cookedLevel <8:
            self.cookedString = "已经烤好了"
        elif self.cookedLevel >=8:
            self.cookedString = "已经烤成木炭了....." 
        
    def addCondliments(self,item):
        self.condiments.append(item)

digua = SweetPotato()

digua.cook(1)
print(digua)
digua.addCondliments("辣椒粉")
digua.cook(1)
print(digua)
digua.addCondliments("酱油")
digua.cook(1)
print(digua)
digua.addCondliments("大蒜")
digua.cook(1)
print(digua)
digua.addCondliments("芥末")
digua.cook(1)
print(digua)
digua.addCondliments("番茄酱")

digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
