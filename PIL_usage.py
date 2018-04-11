#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-2-5 下午4:35
# @Author  : Evan
# @Site    : 
# @File    : PIL_usage.py
# @Software: PyCharm Community Edition
from PIL import Image
import numpy as np
import os

# image = Image.open('/home/yn/Pictures/witch.jpg')
# out = image.resize((256, 256), Image.ANTIALIAS)
# out.save('/home/yn/Pictures/witch_out.jpg')

# height = 256
# width = height * 2
# images = ['/home/yn/Pictures/witch_out.jpg', '/home/yn/Pictures/witcher_out.jpg']
# box = Image.new('RGB', (width, height))
# for i in range(2):
#     image = Image.open(images[i])
#     box.paste(image, (i*256, 0))
# box.save('/home/yn/Pictures/splice_witch.jpg')

# np.set_printoptions(threshold='nan')
# im = Image.open('/home/yn/Pictures/test123.png')
#
# reim = im.convert('L')
# band = reim.getbands()
# mode = reim.mode
# size = reim.size
# print band,mode,size
# reim = reim.resize((28, 28), Image.ANTIALIAS)
# reim.save('/home/yn/Pictures/test11_28*28.png')
#
# imm = Image.open('/home/yn/Pictures/test11_28*28.png')
# data = imm.getdata()
# # data = list(data)
# data = np.array(data)
# print data

np.set_printoptions(threshold='nan')

path_im_train_28 = '/home/yn/Test/TF/tflearn-speech-recognition-master/data/more_detal/new_data_10/train_image/train_image_28*28/'
path_im_test_28 = '/home/yn/Test/TF/tflearn-speech-recognition-master/data/more_detal/new_data_10/test_image/test_image_28*28/'

train_images = os.listdir(path_im_train_28)
test_images = os.listdir(path_im_test_28)

train_input_batch = []
train_label_batch = []
test_input_batch = []
test_label_batch = []


def my_get_speakers(path):
    files = os.listdir(path)
    speakers = list(set(map(my_speaker, files)))
    print('************\nspeech_data.my_get_speakers:\n%d speakers: %s\n************' % (len(speakers), speakers))
    return speakers


def my_speaker(filename):  # vom Dateinamen
    # if not "_" in file:
    #   return "Unknown"
    return filename.split("_")[0]


def one_hot_from_item(item, items):  # item is a iterator
    # items=set(items) # assure uniqueness
    x = [0] * len(items)  # numpy.zeros(len(items))
    i = items.index(item)
    x[i] = 1
    return x


speakers = my_get_speakers(path_im_train_28)

for x in train_images:
    im = Image.open(path_im_train_28 + x)
    data = im.getdata()
    # data = list(data)
    data = np.array(data)
    print data
    train_input_batch.append(data)
    train_label_batch.append(one_hot_from_item(my_speaker(x), speakers))

for x in test_images:
    im = Image.open(path_im_test_28 + x)
    data = im.getdata()
    data = np.array(data)
    test_input_batch.append(data)
    test_label_batch.append(one_hot_from_item(my_speaker(x), speakers))

train_input_batch = np.array(train_input_batch)
train_label_batch = np.array(train_label_batch)
test_input_batch = np.array(test_input_batch)
test_label_batch = np.array(test_label_batch)

print train_input_batch.shape, len(train_input_batch)
print train_label_batch, len(train_label_batch)
print len(test_input_batch[0]), len(test_input_batch)
print len(test_label_batch[0]), len(test_label_batch)
