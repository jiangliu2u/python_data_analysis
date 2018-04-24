import pandas as pd
import matplotlib.pyplot as plt
import requests


match_id= input("请输入职业比赛id:\n")
data = requests.get("https://api.opendota.com/api/matches/"+str(match_id)).json()

gold_change = pd.Series(data['radiant_gold_adv'])
xp = pd.Series(data['radiant_xp_adv'])
fig = plt.figure(figsize=(14,7))#新建图像，figsize为图像大小
ax1 = fig.add_subplot(2,2,1)#添加子图，个数为1*1,第三个1为子图的索引
gold,=ax1.plot(gold_change.index,gold_change.values,color="b")#plot画折线图，x轴为gold和xp索引，此处为比赛时间，纵轴为gold_chang和xp差值，表示带数据点
xp,=ax1.plot(xp.index,xp.values,color="r")#在同一个子图上画经验差变化
ax1.spines['top'].set_color('none')#去除上边框线
ax1.spines['right'].set_color('none')#去除右边框
ax1.set_xlabel("时间（min）")#x轴标签
ax1.text(-10,(list(ax1.axes.get_ylim())[1])/2,str(data['radiant_team']['tag']),rotation=90,fontsize=13,color='k')#添加文字说明，前两个表示文字坐标，rotation旋转角度
ax1.text(-10,(list(ax1.axes.get_ylim())[0])/2,str(data['dire_team']['tag']),rotation=90,fontsize=13,color='k')
ax1.spines['bottom'].set_position(('data', 0))#设置x轴的到数据为0的位置
ax1.spines['left'].set_position(('data', 0))#设置y轴的到数据为0的位置
ax1.set_title("{} vs {} 经济、经验差".format(data['radiant_team']['tag'],data['dire_team']['tag']))#设置标题
ax1.legend(handles=[gold,xp],labels=["经济","经验"],loc='upper left')#设置图例

#拉野情况
laye = {i['name']:i['camps_stacked'] for i in data['players']}
la = pd.Series(laye)
ax2 = fig.add_subplot(222)
a=la.sort_values(ascending=True)
b=a[a.values>0]
names = [i for i in b.index]
haha =pd.Series(names)
ax2.spines['top'].set_color('none')#去除上边框线3846888523
ax2.spines['right'].set_color('none')#去除右边框
ax2.set_yticklabels(haha.values)
ax2.set_yticks(haha.index)
ax2.set_title("堆叠野怪次数")
ax2.barh(range(len(haha.index)),b.values,color='g')#水平条形图

#选手金钱变化
player_gold = {i['name']:i['gold_t'] for i in data['players']}
gold_t = pd.DataFrame(player_gold)
ax3 = fig.add_subplot(2,2,4)
lines = []
ax3.spines['top'].set_color('none')
ax3.spines['right'].set_color('none')
for i in range(10):
	locals()['p{}'.format(i)], = ax3.plot(gold_t.index,gold_t[gold_t.columns[i]])#批量命名变量用到locals函数
	lines.append(locals()['p{}'.format(i)])

ax3.set_title("{} vs {} 选手金钱变化".format(data['radiant_team']['tag'],data['dire_team']['tag']))#设置标题
ax3.legend(handles=lines,labels=list(gold_t.columns),loc='upper left')#设置图例
fig.savefig('{}.png'.format(match_id))
#plt.show()




