#!/usr/bin/env python
# encoding: utf-8
# 统计nginx访问日志中，访问ip数top10,定义为一个函数，传递文件路径，ip访问最高的前n排行。


def ngx_access(file_name,topn):

    temp='|{ip:<16}|{url:<80}|{state:<5}|{count:<5}|'

    dic={}

    fhandler=open(file_name,'rt')
    top10=open('/tmp/nginx_access_{}.txt'.format(topn),'wt')

    for line in fhandler.readlines():
        Line = line.split(' ')
        #if (Line[0],Line[6],Line[8]) not in dic.keys():
        #    dic[(Line[0],Line[6],Line[8])] = 1
        #else:
        #    dic[(Line[0],Line[6],Line[8])] += 1
        tup = (Line[0],Line[6],Line[8])
        dic[tup]=dic.get(tup,0)+1

    fhandler.close()

    D=list(dic.items())

    #for j in range(topn):
    #    for i in range(len(D)-1):
    #        if D[i][1] > D[i+1][1]:
    #            D[i],D[i+1] = D[i+1],D[i]
    
    # 使用sortd函数，lambda函数进行排序
    D=sorted(D,key=lambda x:x[1])

    print('|{0:<16}|{1:<80}|{2:<5}|{3:<5}|'.format('ip','url','state','count'))
    print('-'*111)
    top10.write('|{0:<16}|{1:<80}|{2:<5}|{3:<5}|'.format('ip','url','state','count'))
    top10.write('\n')
    top10.write('-'*111)
    top10.write('\n')
    length = topn+1
    for i in D[-1:-length:-1]:
        print(temp.format(ip=i[0][0],url=i[0][1],state=i[0][2],count=i[1]))
        print('-'*111)
        content=temp.format(ip=i[0][0],url=i[0][1],state=i[0][2],count=i[1])
        top10.write(content)
        top10.write('\n')
    top10.close()

#ngx_access("/root/python/access.txt",10)
#ngx_access("/usr/local/nginx/logs/access.log",topn)

content=input('请输入您想要查询的文件名，和显示的排名行数(filename,linenumber): ')
file_name=content.split(',')[0]
topn=int(content.split(',')[1])
ngx_access(file_name,topn)
