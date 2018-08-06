import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from keras.layers import Dense
from keras.models import Sequential


def interpolate_data(data, location, k=5):
    """
    Args:
        data:需要插值的列，DataFrame列，
        location：插值的位置
        k：插入位置前后数值的个数的，默认5
    """
    y = data[list(range(location - k, location)) + list(range(location + 1, location + 1 + k))]
    y = y[y.notnull()]  # 前后参考值不能为空
    return lagrange(y.index, list(y))(location)


def main():
    raw_data = pd.read_excel("car.xls", index_col=0)
    data = raw_data.iloc[:, 2:]  # 取有效的数据，从第三列开始到最后一列
    # 把正常设置为0，漏税为1
    for i in range(len(data)):
        if data.iloc[i, -1] == "正常":
            data.iloc[i, -1] = 0
        else:
            data.iloc[i, -1] = 1
    # 逐列插值,最后输出的一列除外,此处不需要插值，数据为0
    # for i in range(len(data.columns)-1):
    #     for j in range(len(data)):
    #         if data.iloc[j,i]==0:
    #             data.iloc[j,i] = interpolate_data(data.iloc[:,i],j)
    train = data.as_matrix()

    # keras神经网络模型
    model = Sequential()
    model.add(Dense(32, activation='relu', input_dim=12))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(train[:, :-1], train[:, -1], epochs=200, batch_size=50, verbose=1)
    predicted_result = model.predict_classes(train[:, :-1], batch_size=20).reshape(len(train))
    print(train[:, -1], predicted_result)
    score = model.evaluate(train[:, :-1], train[:, -1], batch_size=128)
    print("loss:{},accuracy:{}".format(score[0], score[1]))
    from plot import plot_cm
    plot_cm(train[:, -1], predicted_result, 'keras NN')
    
    # CART决策树
    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier()
    tree.fit(train[:, :-1], train[:, -1])
    plot_cm(train[:, -1], tree.predict(train[:, :-1]), 'CART')
    plt.show()


if __name__ == '__main__':
    main()
