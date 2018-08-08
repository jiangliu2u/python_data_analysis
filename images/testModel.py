from keras.preprocessing.image import img_to_array, load_img, image
from keras.models import load_model
import numpy as np
import glob

#加载权重
model = load_model("butterflies.hdf5")

#获取当前目录下所有jpg照片
imgs = glob.glob("*.jpg")
for i in imgs:
    #加载图片，target_size必须与model训练时一样
    img = load_img(i,target_size=(200,200))
    img = image.img_to_array(img)/255.0
    img = np.expand_dims(img,axis=0)

    #预测图片的种类，返回训练时的类的序号
    predictions = model.predict_classes(img)
    print(predictions)

