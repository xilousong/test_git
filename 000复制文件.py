#!/usr/bin/env python3

# 获取想要复制的文件
file = input("请输入您要复制的文件名：")
file_name = file.strip().lstrip().rstrip()

# 打开原文件
file_origin = open(file_name,"r")


# 定义拷贝后的文件名
file_copyname = file_name.split(".")[0] + "[复件]" + ".txt"
    
# 创建拷贝后的文件
file_copy = open(file_copyname,"w")

# 这里用while循环 控制每次读取的内容的大小，防止在读取太大的文件时内
# 内存的溢出
while True:

    # 获取原文件的内容
    content = file_origin.read(1024)
    
    # 将原文件的内容写入拷贝文件
    file_copy.write(content)

    if len(content) == 0:
        break

# 关闭文件
file_origin.close()
file_copy.close()





