import pandas as pd

inputfile = "consumption_data.xls"
outputfile = "data_type.xls"
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

k = 3
iteration = 500
data = pd.read_excel(inputfile, index_col="Id")

data_zs = 1.0 * (data - data.mean()) / data.std()
pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data)


def density_plot(data):
    return fig


# pprint(rint(data_zs)
from sklearn.cluster import KMeans

if __name__ == "__main__":
    model = KMeans(n_clusters=3, n_jobs=4, max_iter=iteration)  # 多CPU计算必须放在if __name__=="__main__"中
    model.fit(data_zs)

    r1 = pd.Series(model.labels_).value_counts()
    r2 = pd.DataFrame(model.cluster_centers_)
    r = pd.concat([r1, r2], axis=1)
    r.columns = list(data.columns) + ['nums of class']
    r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
    r.columns = list(data.columns) + ['nums of cluster']
    data2 = pd.read_excel("data_type.xls")
    c0 = data2[data2['nums of cluster'] == 0]
    c1 = data2[data2['nums of cluster'] == 1]
    c2 = data2[data2['nums of cluster'] == 2]
    print(c1.iloc[1].index[0])
    a = [c0, c1, c2]
    for j in range(len(a)):
        fig, axes = plt.subplots(3, 1)
        for i in range(4):
            if a[j].columns[i] != "Id":
                a[j].iloc[:, i].plot(kind='kde', title="cluster{} density".format(j),ax=axes[i - 1], label=a[j].columns[i])
                axes[i - 1].legend()
        fig.show()
        fig.savefig("c{}.png".format(j))
