#!/usr/bin/env python3

f = open("/root/python/file_read.txt","w")

mess = """ hello world ,nice to meet you ,i am very glad to see you agin!!
        see you tomorome, hahahhaha
         aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
cccccccccccccccccccccccccccccccc  

"""
f.write(mess)

f.close()
