import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

data = pd.read_excel("iris.xls")
km =KMeans(n_clusters=3,max_iter=200)
km.fit(data.iloc[:,0:3])

dataz = 1*(data-data.mean())/data.std()
pca = PCA(n_components=3)
new_data=pca.fit_transform(dataz.iloc[:,0:3])
newD = pd.DataFrame(new_data)
newD['c']=km.labels_
fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
for i in range(150):
    if newD.iloc[i,-1]==0:
        ax.scatter(newD.iloc[i,0],newD.iloc[i,1],newD.iloc[i,2],color='b')
    if newD.iloc[i,-1]==1:
        ax.scatter(newD.iloc[i,0],newD.iloc[i,1],newD.iloc[i,2],color='g')
    if newD.iloc[i,-1]==2:
        ax.scatter(newD.iloc[i,0],newD.iloc[i,1],newD.iloc[i,2],color='r')
plt.show()