#coding=utf-8
import numpy as np
#
#
# lab = np.load("data2/label.npy")
# for i in range(0, 5):
#     num = np.where(lab == i)
#     print num[0].shape[0]
# train_lab = np.load("lab/train_lab2.npy")
# for i in range(1, 5):
#     num = np.where(train_lab == i)
#     print num[0].shape[0]
# for i in range(12944):
#     for j in range(2820):
#         if(lab[i,j] == train_lab[i,j]):
#             lab[i, j] = 0
# np.save("data2/test_lab.npy",lab)
# for i in range(0, 5):
#     num = np.where(lab == i)
#     print num[0].shape[0]

# from PIL import Image
import skimage.io
import scipy.io as sio
import h5py
from collections import Counter
from constant import *
data_col = data4_col
data_row = data4_row
im = h5py.File('train_data/data3/sp3000.mat')
super = np.array(im['L'], dtype=int)
super = super.T
max = int(np.max(super))
min = int(np.min(super))
print (max, min)
label = np.load('Result/data3_result10%/alltest_y1_35000deal_med.npy')
imglab = np.zeros((data_row, data_col))
for i in range(min, (max+1)):
    print (i)
    demo = []
    index = np.where(super == i)
    for j in range(index[0].shape[0]):
        demo.append(label[index[0][j], index[1][j]])
    num = Counter(demo).most_common(int(index[0].shape[0] * 0.9))
    lab = num[0][0]
    for M in range(index[0].shape[0]):
        label[index[0][M], index[1][M]] = lab
np.save('Result/data3_result10%/alltest_y1_35000deal_med_super3000.npy', label)
# print (Counter(demo).most_common(int(index[0].shape[0] * 0.9)))
# print ('ok')


