import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout
import numpy as np
import pandas as pd

data = pd.read_excel('iris.xls', header=None)
print(data)
data = data.as_matrix()  # 转化为np.array

X = data[:,0:3]
y = keras.utils.to_categorical(data[:, -1], 3)

model = Sequential()  # 序贯式模型
model.add(Dense(512, activation='relu', input_dim=3))
model.add(Dropout(0.2))  # 防止过拟合，每次更新参数时随机断开一定百分比（rate）的输入神经元
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3, activation='softmax'))

model.compile(loss="categorical_crossentropy",optimizer='rmsprop', metrics=["accuracy"])

history=model.fit(X, y,batch_size=5,epochs=200,verbose=1)
score = model.evaluate(X,y)
print("loss:{},accuracy:{}".format(score[0],score[1]))


