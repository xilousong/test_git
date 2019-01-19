#encoding:utf-8

class Dhh():
    def __init__(self):
        self.dian = 0
        self.status = "没开"

    def __str__(self):
        return "水已经烧了%d 分钟，现在的状态是 %s"%(self.dian,self.status)

    def Dian(self,time):
        self.dian += time
        if self.dian >1 and self.dian <= 5:
            self.status = "水还没开"
        elif self.dian >5 and self.dian <= 8:
            self.status = "水快开了，还差一点点..."
        elif self.dian > 8:
            self.status = "水开了..."

dhh1 = Dhh()
dhh1.Dian(9)
print(dhh1)
