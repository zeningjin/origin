from PIL import Image
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import os
import numpy as np
import pickle

dir_path = r'D:\workplace\人工智能\手工数字识别\image'

# 需要构建特征矩阵和目标向量
Y = []
datas = []
for file in os.listdir(dir_path):
    Y.append(file.split('_')[0])
    img = Image.open(os.path.join(dir_path,file))
img=np.array(img)
print(img)
#     r_img,g_img,b_img=img.split()
#     r_img=np.array(r_img)
#     g_img = np.array(g_img)
#     b_img = np.array(b_img)
#     # 计算一阶颜色距
#     r1=r_img.mean()
#     g1=g_img.mean()
#     b1=b_img.mean()
#     # 计算二阶颜色距
#     r2=r_img.std()
#     g2=g_img.std()
#     b2=b_img.std()
#     # 计算三阶颜色距
#     r3=(((r_img-r1)**3).mean())**1/3
#     g3 = (((g_img - r1) ** 3).mean()) ** 1 / 3
#     b3 = (((b_img - r1) ** 3).mean()) ** 1 / 3
#     datas.append([r1,r2,r3,g1,g2,g3,b1,b2,b3])
# datas=np.array(datas)
# Y = np.array(Y)
# s = StandardScaler()
# X = s.fit_transform(datas)
# train_x,test_x,train_y,test_y = train_test_split(X,Y)
# svm=SVC()
# svm.fit(train_x,train_y)
# print(svm.score(test_x,test_y))