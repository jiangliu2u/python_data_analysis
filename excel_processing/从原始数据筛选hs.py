import pandas as pd
import datetime
start = datetime.datetime.now()
input_file = "aa.xls"
output_file = "hs.xls"

data = pd.read_excel(input_file,header=[1])
companies = [2119,2144, 2552, 2543, 2620, 2549, 2617, 2137, 2590, 2783, 2731, 2580,
             2592, 2561, 2551, 2738, 2550, 2611, 2587, 2618, 2596, 2626, 2581, 2644]  # 分公司代码
outdata1 = data[ data["工厂"].isin(companies)]
outdata1 = outdata1.reset_index(drop=True)
outdata1.to_excel(output_file)
print("筛选hs数据完成，文件名为 {}".format(output_file))
end = datetime.datetime.now()
print("运行时间 {}".format(end - start))

