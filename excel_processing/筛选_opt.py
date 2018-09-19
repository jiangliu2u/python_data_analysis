import pandas as pd
import datetime
start = datetime.datetime.now()
input_file = "hs.xls"  #原始文件名称
output_file = "final2.xls" #输出文件名称

#读取hs所有信息
hs_data = pd.read_excel(input_file)

data = pd.concat([hs_data["工厂描述"],hs_data["产品名称"],hs_data["材料名称"],hs_data["理论消耗量"],hs_data["实际消耗量"]],axis=1)
data1 = data[data["材料名称"].str.contains("盖")]
data2 = data1[~data1["材料名称"].str.contains("待切|瓶盖料|内垫料")]
data3 = data2[~data2["产品名称"].str.contains("空罐|底盖")]
data3 = data3.reset_index(drop=True)
data3.index.name = "序号"
data3.to_excel(output_file)


print("进一步筛选数据完成，文件名为 {}".format(output_file))
end = datetime.datetime.now()
print("运行时间 {}".format(end - start))

