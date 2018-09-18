import pandas as pd
import datetime
start = datetime.datetime.now()
input_file = "aa.xls"
output_file = "hs.xls"

data = pd.read_excel(input_file,header=[1])

companies = [2119,2144, 2552, 2543, 2620, 2549, 2617, 2137, 2590, 2783, 2731, 2580,
             2592, 2561, 2551, 2738, 2550, 2611, 2587, 2618, 2596, 2626, 2581, 2644]  # 分公司代码

index_com = []
for i  in companies:
    d = data[data['工厂'] == i].index.tolist()
    for j in d:
        index_com.append(j)

index_com = list(set(index_com))
ff = []
for i in index_com:
    ff.append(data.iloc[i, :])  # 根据索引选择行，保存在ff中，再转化为DataFrame导出为excel
outdata1 = pd.DataFrame(ff)
outdata1 = outdata1.reset_index(drop=True)
outdata1.to_excel(output_file)
end = datetime.datetime.now()
print("筛选hs数据完成，文件名为 {}".format(output_file))
print("运行时间 {}".format(end - start))

