#!/usr/bin/env python3
# encoding: utf-8

users={}

text= """ ----用户管理系统 V-1.0.0----
        请按提示进行输入要执行的操作
          add :   添加用户
          del :   删除用户
          update: 编辑用户信息
          list:   列出用户信息
          find:   查找用户
          exit/q: 退出系统
"""

print(text)

while True:
    INPUT=input('请输入要执行的操作：')
    per={}
    
    if INPUT == "add":
        new_user=input("请输入用户信息格式(用户名:年龄:联系方式): ").strip()
        if (len(new_user.split(':')) != 3) or (not new_user.split(':')[1].isdigit()):
            print('您的输入有误，请重新输入。')
        #if new_user.split(':')[0] in users.keys():
        #    print("此用户已经存在！！！")
        #    continue
        else:
            uid = len(users)+1
            per['name']= new_user.split(":")[0]
            per['age']= int(new_user.split(":")[1])
            per['tel']= new_user.split(":")[2]
            users[uid]=per
            print('用户添加成功！！！')
            print(users)

    if INPUT == "del":
        input_txt=int(input("请输入要删除的用户ID："))
        if input_txt not in users.keys():
            print("此用户不存在！！！")
        else:
            print(users[input_txt])
            panduan=input('您确定要删除此用户吗(yes/no): ')
            if panduan == 'yes':
                print('删除成功，您删除的用户是{0}'.format(users[input_txt]['name']))
                del users[input_txt]

    if INPUT == "update":
        input_txt=int(input("请输入要修改的用户ID："))
        if input_txt not in list(users.keys()):
            print("此用户不存在！！！")
        else:
            new_user=input("请输入要更新的用户信息，格式(用户名:年龄:联系方式): ")
            if (len(new_user.split(':')) != 3) or (not new_user.split(':')[1].isdigit()):
                print('您的输入有误，请重新输入。')

           # if new_user.split(':')[0] not in users.keys():
           # print("此用户不存在！！！")
           #   continue
            else:
                users[input_txt]['name']=new_user.split(':')[0]
                users[input_txt]['age']=int(new_user.split(':')[1])
                users[input_txt]['tel']=new_user.split(':')[2]

    if INPUT == "find":
        input_txt=input("请输入要查找的用户名：")
        for i in users.items():
            if input_txt == i[1]['name']:
                print("|{0:^5}|{1:^10s}|{2:^5s}|{3:^15s}|".format("ID","姓名","年龄","联系方式"))
                print("|{0:^5}|{1:^10s}|{2:^5d}|{3:^15s}|".format(i[0],i[1]['name'],i[1]['age'],i[1]['tel']))
            #print("此用户不存在！！！")
        #else:
        #    print("|{0:^5}|{1:^10s}|{2:^5s}|{3:^15s}|".format("ID","姓名","年龄","联系方式"))
        #    print("|{0:^5}|{1:^10s}|{2:^5d}|{3:^15s}|".format(users[input_txt]['name'],users[input_txt]['age'],
        #    users[input_txt]['tel']))

    if INPUT == "list":
        print("|{0:^5}|{1:^10s}|{2:^5s}|{3:^15s}|".format("ID","姓名","年龄","联系方式"))
        print('-'*50)
        for k,v in users.items():
            print("|{0:^5}|{1:^10s}|{2:^5d}|{3:^15s}|".format(k,v['name'],v['age'],v['tel']))

    if INPUT == "exit" or INPUT == "q":
        print('谢谢使用！！！')
        break
