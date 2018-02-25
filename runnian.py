#!/usr/bin/env python3
#year=int(input('plz input the year: '))
def Runnian(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
        print("{}是闰年".format(year)) 
    else:
        print("{}不是闰年".format(year))


if  __name__ == "__main__":
    Runnian(2018)

