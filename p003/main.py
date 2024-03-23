# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:16:50 2024

@author: Cai
"""

from netgene import NodeCreate,EdgeCreate
import networkx as nx
from constant import a,b,c
import matplotlib.pyplot as plt


G=nx.Graph()
#得到所有元素
temp=NodeCreate(a)
#得到单元素字典的键和值
dicList=EdgeCreate(a)

#建立节点
for item in temp:
    G.add_node(item)

#建立边
for item in dicList:
    (key, value),=item.items()
    G.add_edge(key,value)


#以下为绘图设置（待完善）
#pos=nx.spring_layout(G)
pos=nx.kamada_kawai_layout(G)
#pos=nx.fruchterman_reingold_layout(G)
#根据名字筛选上级节点，改变颜色
color_map=[]
for node in G:
    if "类" in node:
        color_map.append('red')
    else:
        color_map.append('cyan')
#调整画幅
plt.rcParams['figure.figsize']=(45,45)
#节点名字是汉字时，需添加
plt.rcParams['font.sans-serif']='SimHei'
#节点尺寸、字号、布局、颜色
nx.draw(G,pos=pos,node_size=500,node_color=color_map,with_labels=False)
nx.draw_networkx_labels(G,pos=pos,font_size=8)
plt.show()
