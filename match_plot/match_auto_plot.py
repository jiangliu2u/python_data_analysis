import pandas as pd
import matplotlib.pyplot as plt
import json
import requests


match_id= input("请输入职业比赛id:\n")
data = requests.get("https://api.opendota.com/api/matches/"+str(match_id)).json()

gold_change = pd.Series(data['radiant_gold_adv'])
xp = pd.Series(data['radiant_xp_adv'])
fig = plt.figure(figsize=(8,8))#新建图像，figsize为图像大小
ax1 = fig.add_subplot(1,1,1)#添加子图，个数为1*1,第三个1为子图的索引
gold,=ax1.plot(gold_change.index,gold_change.values,color="b",marker='o')#plot画折线图，x轴为gold_change索引，此处为比赛时间，纵轴为gold_change值，marker=‘o’表示带数据点
xp,=ax1.plot(xp.index,xp.values,color="r")#在同一个子图上画经验差变化
ax1.spines['top'].set_color('none')#去除上边框线
ax1.spines['right'].set_color('none')#去除右边框
ax1.set_xlabel("times/min")#x轴标签
ax1.text(-6,3600,str(data['radiant_team']['name']),rotation=90,fontsize=13,color='k')#添加文字说明，前两个表示文字坐标，rotation旋转角度
ax1.text(-6,-4000,str(data['dire_team']['name']),rotation=90,fontsize=13,color='k')
ax1.spines['bottom'].set_position(('data', 0))#设置x轴的到数据为0的位置
ax1.spines['left'].set_position(('data', 0))#设置y轴的到数据为0的位置
ax1.set_title("{} vs {} 经济、金钱差".format(data['radiant_team']['name'],data['dire_team']['name']))#设置标题
ax1.legend(handles=[gold,xp],labels=["gold","xp"],loc='best')#设置图例
plt.show()#显示图片


laye = {}#拉野
for i in data["players"]:
    laye[i['name']]=i['camps_stacked']
la = pd.Series(laye)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
a=la.sort_values(ascending=True)
b=a[a.values>0]
names = [i for i in b.index]
haha =pd.Series(names)
ax2.spines['top'].set_color('none')#去除上边框线3846888523
ax2.spines['right'].set_color('none')#去除右边框
ax2.set_yticklabels(haha.values)
ax2.set_yticks(haha.index)
ax2.barh(haha.index,b.values,color='c')
fig2.savefig('d.png')
plt.show()