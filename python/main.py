from __future__ import absolute_import
import numpy as np
import csv
import tensorflow as tf

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD

import pandas as pd

from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

from sklearn import svm, metrics
import keras
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import load_model

from PIL import Image
import glob
import os

tf.logging.set_verbosity(tf.logging.ERROR)

# size = 48, 48
img = load_img('test3.png')
img = img.resize((48, 48), Image.ANTIALIAS)


# img = load_img('test_final2.png') 
X_train = img_to_array(img)
# print X_train.shape
X_train = np.mean(X_train, axis=2)
# print X_train.shape
# X_train = X_train.reshape(3, 48, 48)
X_train = X_train.reshape((1,) + (48,48,1))
# print X_train.shape
# print X_train.shape
# X_train = X_train.reshape(X_train.shape[0], 48, 48, 3)
X_train = X_train.astype("float32")
X_train /= 255

# x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
# x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
# print x.shape



model = load_model('Deep_Net_Final.h5')

# predict_classes(self, x, batch_size=32, verbose=1)
predictions = model.predict_classes(X_train, batch_size=1, verbose=1)
print predictions[0]