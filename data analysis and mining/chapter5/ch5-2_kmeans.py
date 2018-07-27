import pandas as pd
inputfile ="consumption_data.xls"
outputfile ="data_type.xls"
from sklearn.decomposition import PCA
k=3
iteration = 500
data = pd.read_excel(inputfile,index_col = "Id")

data_zs = 1.0 * (data-data.mean())/data.std()
pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data)

#pprint(rint(data_zs)
from sklearn.cluster import KMeans
if __name__=="__main__":
    model = KMeans(n_clusters=3,n_jobs=4,max_iter = iteration)#多CPU计算必须放在if __name__=="__main__"中
    model.fit(data_zs)


    r1 = pd.Series(model.labels_).value_counts()
    r2 = pd.DataFrame(model.cluster_centers_)
    r = pd.concat([r1,r2],axis=1)
    r.columns = list(data.columns)+['nums of class']
    r = pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
    r.columns = list(data.columns)+['nums of cluster']
    data2 = pd.read_excel("data_type.xls",index_col="Id") 
    import matplotlib.pyplot as plt
    for i in range(k):
        for j in range(len(data2.iloc[0])):
           (data2[data2['nums of cluster']==i].iloc[:,3]).plot(kind ="kde",subplots=True)
    #data2.plot(kind='kde',subplots =True)
    plt.show()
