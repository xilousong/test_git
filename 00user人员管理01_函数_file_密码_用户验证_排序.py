#!/usr/bin/env python3
# encoding: utf-8

import json

path='users.data.txt'

users={}

login=False

def login_auth():
    global login
    login=False

    fhandler = open('users.data.txt','rt')
    for line in fhandler.readlines():
        nodes = line.strip().split(',')
        # ID=int(nodes[0])
        # name=nodes[1]
        # age=int(nodes[2])
        # tel=nodes[3]
        users[int(nodes[0])]={'name':nodes[1],'age':int(nodes[2]),'tel':nodes[3],'password':nodes[4]}
    fhandler.close()

    #for i in range(3):
    for i in range(3):
        txt=input('请输入验证信息(用户名/密码): ')
        username,password = txt.split('/')
        for k,user in users.items():
            if user['name'] == username and user['password'] == password:
                login=True  
                break
        if login:
            print('登录成功。')
            break
        else:
            print('用户名或密码输入错误，请重新输入。')
    else:
        print("连续3次验证失败，已退出。")

    if login:
        print('登录成功。')

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
    

def add():
    new_user=input("请输入用户信息格式(用户名:年龄:联系方式:密码): ").strip()
    if (len(new_user.split(':')) != 4) or (not new_user.split(':')[1].isdigit()):
        print('您的输入有误，请重新输入。')
    #if new_user.split(':')[0] in users.keys():
    #    print("此用户已经存在！！！")
    #    continue
    else:
        uid = len(users)+1
        per['name']= new_user.split(":")[0]
        per['age']= int(new_user.split(":")[1])
        per['tel']= new_user.split(":")[2]
        per['password']=new_user.split(':')[3]
        users[uid]=per
        print('用户添加成功！！！')
        users_json=json.dumps(users)
        print(users_json)
        fhandler = open('users.data.txt','wt')
        for k,v in users.items():
            fhandler.write('{0},{1},{2},{3},{4}\n'.format(k,v['name'],v['age'],v['tel'],v['password']))
        fhandler.close()


def delete():
    input_txt=int(input("请输入要删除的用户ID："))
    if input_txt not in users.keys():
        print("此用户不存在！！！")
    else:
        print(users[input_txt])
        panduan=input('您确定要删除此用户吗(yes/no): ')
        if panduan == 'yes':
            print('删除成功，您删除的用户是{0}'.format(users[input_txt]['name']))
            del users[input_txt]
            fhandler = open('users.data.txt','wt')
            for k,v in users.items():
                fhandler.write('{0},{1},{2},{3},{4}\n'.format(k,v['name'],v['age'],v['tel'],v['password']))
            fhandler.close()


def update():
    #yanzhen = input('请输入验证信息(用户名/密码):')
    #yz_list=list(yanzhen.split('/'))
    #for k,v in users.items():
    #    if (yz_list[0] == v['name']) and (yz_list[1] == v['password']):
    input_txt=int(input("请输入要修改的用户ID："))
    if input_txt not in list(users.keys()):
        print("此用户不存在！！！")
    else:
        new_user=input("请输入要更新的用户信息，格式(用户名:年龄:联系方式): ")
        if (len(new_user.split(':')) != 4) or (not new_user.split(':')[1].isdigit()):
            print('您的输入有误，请重新输入。')

       # if new_user.split(':')[0] not in users.keys():
       # print("此用户不存在！！！")
       #   continue
        else:
            users[input_txt]['name']=new_user.split(':')[0]
            users[input_txt]['age']=int(new_user.split(':')[1])
            users[input_txt]['tel']=new_user.split(':')[2]
            users[input_txt]['password']=new_user.split(':')[3]
            fhandler = open('users.data.txt','wt')
            for k,v in users.items():
                fhandler.write('{0},{1},{2},{3},{4}\n'.format(k,v['name'],v['age'],v['tel'],v['password']))
            fhandler.close()


def find():
    fhandler = open('users.data.txt','rt')
    for line in fhandler.readlines():
        nodes = line.strip().split(',')
         # ID=int(nodes[0])
       # name=nodes[1]
       # age=int(nodes[2])
       # tel=nodes[3]
        users[int(nodes[0])]={'name':nodes[1],'age':int(nodes[2]),'tel':nodes[3],'password':nodes[4]}
    fhandler.close()
    input_txt=input("请输入要查找的用户名：")
    for i in users.items():
        if input_txt == i[1]['name']:
            print("|{0:<5}|{1:<6s}|{2:<3s}|{3:<15s}|{4:<15s}|".format("ID","姓名","年龄","联系方式","密码"))
            print("|{0:<5}|{1:<8s}|{2:<5d}|{3:<19s}|{4:<15s}|".format(i[0],i[1]['name'],i[1]['age'],i[1]['tel'],
            '*'*len(i[1]['password'])))
        #print("此用户不存在！！！")
    #else:
    #    print("|{0:^5}|{1:^10s}|{2:^5s}|{3:^15s}|".format("ID","姓名","年龄","联系方式"))
    #    print("|{0:^5}|{1:^10s}|{2:^5d}|{3:^15s}|".format(users[input_txt]['name'],users[input_txt]['age'],
    #    users[input_txt]['tel']))


def List():
    fhandler = open('users.data.txt','rt')
    for line in fhandler.readlines():
        nodes = line.strip().split(',')
       # ID=int(nodes[0])
       # name=nodes[1]
       # age=int(nodes[2])
       # tel=nodes[3]
        users[int(nodes[0])]={'name':nodes[1],'age':int(nodes[2]),'tel':nodes[3],'password':nodes[4]}
    fhandler.close()
    print("|{0:<5s}|{1:<6s}|{2:<3s}|{3:<15s}|{4:<15s}|".format("ID","姓名","年龄","联系方式","密码"))
    print('-'*60)
   
    new_list=list(users.values())
    lenth = len(new_list)
    pxziduan = input('请输入您要排序的字段(name/age/tel):')
    if pxziduan == 'name':
        while lenth:
            for i in range(lenth -1):
                if new_list[i]['name'] > new_list[i+1]['name']:
                    new_list[i],new_list[i+1]=new_list[i+1],new_list[i]
            lenth -= 1    
        
        for i in new_list:             
            for k,v in users.items():
                if i['name'] == v['name']: 
                    print("|{0:<5d}|{1:<8s}|{2:<5d}|{3:<19s}|{4:<15s}|".format(k,v['name'],v['age'],v['tel'],'*'*len(v['password'])))
    if pxziduan == 'age':
        while lenth:
            for i in range(lenth -1):
                if new_list[i]['age'] > new_list[i+1]['age']:
                    new_list[i],new_list[i+1]=new_list[i+1],new_list[i]
            lenth -= 1    
        
        for i in new_list:             
            for k,v in users.items():
                if i['age'] == v['age']: 
                    print("|{0:<5d}|{1:<8s}|{2:<5d}|{3:<19s}|{4:<15s}|".format(k,v['name'],v['age'],v['tel'],'*'*len(v['password'])))
    
    if pxziduan == 'tel':
        while lenth:
            for i in range(lenth -1):
                if new_list[i]['tel'] > new_list[i+1]['tel']:
                    new_list[i],new_list[i+1]=new_list[i+1],new_list[i]
            lenth -= 1    
        
        for i in new_list:             
            for k,v in users.items():
                if i['tel'] == v['tel']:
                    print("|{0:<5d}|{1:<8s}|{2:<5d}|{3:<19s}|{4:<15s}|".format(k,v['name'],v['age'],v['tel'],'*'*len(v['password'])))
     
       
def quit():
    print('谢谢使用！！！')


def main():
    login_auth()
    while login:
        INPUT=input('请输入要执行的操作：')
        per={}
      
        if INPUT == "add":
            add()
        if INPUT == "del":
            delete()
        if INPUT == "update":
            update()
        if INPUT == "find":
            find()
        if INPUT == "list":
            List()
        if INPUT == "exit" or INPUT == "q":
            quit()
            break

if __name__ == "__main__":
    main()
