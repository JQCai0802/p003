# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:17:19 2024

@author: Cai
"""



#输入源数据，输出所有元素名字组成的列表（不去重）
def NodeCreate(a):
    #存储产品门类名
    list01=[]
    #存储产品名
    list02=[]
    #存储企业名
    list03=[]
    #遍历第一级字典，将键入列
    for k,v in a.items():
        list01.append(k)
    #遍历第二级字典，键入列，值合并
        for x,y in v.items():
            list02.append(x)
            list03.extend(y)
    
    return list01+list02+list03

#输入源数据，输出所有单元素字典列表，字典中的内容为有关系的两个元素
#由于同一个字典中不允许有重复的键，所以使用字典列表
def EdgeCreate(a):
    #存储第一级关系（产品门类：产品名）
    dicList01=[]
    #存储第二级关系（产品名：生产企业）
    dicList02=[]
    #遍历数据源
    for k,v in a.items():
        for x,y in v.items():
    #建立产品门类和产品的联系
            dicTemp={k:x}
            dicList01.append(dicTemp)
            for item in y:
    #建立产品和企业的联系
                dicTempNext={x:item}
                dicList02.append(dicTempNext)
    return dicList01+dicList02       
    






