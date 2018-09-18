import pandas as pd
import datetime
start = datetime.datetime.now()
input_file = "hs.xls"  #原始文件名称
output_file = "final.xls" #输出文件名称

#读取hs所有信息
hs_data = pd.read_excel(input_file)

#选取指定的列并按列合并为新的data
data = pd.concat([hs_data["工厂描述"],hs_data["产品名称"],hs_data["材料名称"],hs_data["理论消耗量"],hs_data["实际消耗量"]],axis=1)

temp_index = []#保存包含符合条件的材料名称
for i in data["材料名称"]:
    if '盖' in i and "待切" not in i and "瓶盖料" not in i and "内垫料" not in i:
        h = data[data["材料名称"] == i].index.tolist()  # 获取符合筛选条件材料名称的所有索引，并保存在temp_index里
        for ind in h:
            temp_index.append(ind)

results = []
print(len(temp_index))
temp_index = list(set(temp_index))
print(len(list(set(temp_index))))

for i in temp_index:
    # 根据保存的索引得到data里的数据，保存在results中，再转化为dataFrame导出为excel
    results.append(data.iloc[i,:])

#results为符合条件的材料名称的所有数据
results = pd.DataFrame(results)
results = results.reset_index(drop=True)

# results.to_excel("r.xls")

temp_index2 = []#保存不包含"空罐"的产品名称所在列的索引
for i in results["产品名称"]:
    if "空罐" not in i and "底盖" not in i:
        h = results[results["产品名称"] == i].index.tolist()
        for ind in h:
            temp_index2.append(ind)

final = []
print(len(temp_index2))
print(len(list(set(temp_index2))))
temp_index2 = list(set(temp_index2))
for i in temp_index2:
    # 根据保存不包含"空罐"数据的索引得到results里的数据，保存在final中，再转化为dataFrame导出为excel
    final.append(results.iloc[i,:])
final = pd.DataFrame(final)
final = final.reset_index(drop=True)
final.to_excel(output_file)
print("进一步筛选数据完成，文件名为 {}".format(output_file))
end = datetime.datetime.now()
print("运行时间 {}".format(end - start))

