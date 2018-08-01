# coding: utf-8
import os
import cv2
from numpy import *
def get_images(test_data_path):
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk(test_data_path):
        for i in range(1, 4051):
            filename = 'traindata' + str(i) + '.jpg'
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print 'Find {} images'.format(len(files))
    return files

pre_map = zeros((12960, 2880))
i = 0
j = 0

premap_path = '/home/asdf/Documents/zhanghui/refinenet-image-segmentation-master/123/result'
im_fn_list = get_images(premap_path)
for im_fn in im_fn_list:
    im = cv2.imread(im_fn)
    im = im[:, :, 0]
    # pre_map[i:i+96, j:j+96] = im
    # if j >= 2880:
    #     i = i + 96
    #     j = 0
    # else:
    #     j = j + 96
print ('ok')