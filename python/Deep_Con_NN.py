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

tf.logging.set_verbosity(tf.logging.ERROR)

def faces_load_data():
 
    skip_rows = 1
    train_size = 28709
    test_size = 3589
    dim = 48
    X_train = np.empty([train_size,dim, dim])
    X_test = np.empty([test_size, dim, dim])
    y_train = np.empty(train_size)
    y_test = np.empty(test_size)
    
    f = open('fer2013.csv', 'rb')
 
    train_index = test_index = 0
    for i, line in enumerate(f):
        if i >= skip_rows:
            split_line = line.split(",")
            usage = split_line[2].rstrip()
            if usage == 'Training':
                X_train[train_index, :,:] = np.fromstring(split_line[1], dtype = 'int', sep = ' ').reshape(dim, dim)
                y_train[train_index] = int(split_line[0])
                train_index += 1
            elif usage == 'PublicTest':
                X_test[test_index, :,:] = np.fromstring(split_line[1], dtype = 'int', sep = ' ').reshape(dim, dim)
                y_test[test_index] = int(split_line[0])
                test_index += 1
                 
    return (X_train, y_train) , (X_test, y_test)




np.random.seed(1337)  
    
batch_size = 128
nb_classes = 7
nb_epoch = 1000


img_rows, img_cols = 48, 48
nb_filters = 32
nb_pool = 2
nb_conv = 3

(X_train, y_train), (X_test, y_test) = faces_load_data()

# print (X_train.shape)

X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
X_train = X_train.astype("float32")
X_test = X_test.astype("float32")
X_train /= 255
X_test /= 255
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()

model.add(Convolution2D(32, nb_conv, nb_conv,border_mode='same', input_shape=(img_rows, img_cols, 1)))
# keras.layers.normalization.BatchNormalization()
model.add(Activation('relu'))
model.add(Convolution2D(32, nb_conv, nb_conv))
# keras.layers.normalization.BatchNormalization()
model.add(Activation('relu'))
model.add(Convolution2D(32, nb_conv, nb_conv))
# keras.layers.normalization.BatchNormalization()
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.2))

model.add(Convolution2D(64, 3, 3, border_mode='same'))
# keras.layers.normalization.BatchNormalization()
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
# keras.layers.normalization.BatchNormalization()
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam',  metrics=['accuracy'])

# model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, show_accuracy=True, verbose=1, validation_data=(X_test, Y_test))
# score = model.evaluate(X_test, Y_test, show_accuracy=True, verbose=0)
# print('Test score:', score[0])
# print('Test accuracy:', score[1])

datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)

datagen.fit(X_train)

early_stopping = EarlyStopping(monitor='val_loss', patience=10)

model_checkpoint = ModelCheckpoint('Deep_Net_Draft.h5', monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=False, mode='auto')


model.fit_generator(datagen.flow(X_train, Y_train, batch_size=128), validation_data=(X_test,Y_test),
                    samples_per_epoch=len(X_train), nb_epoch=nb_epoch, callbacks=[early_stopping, model_checkpoint])
# model.save('Deep_NetF.h5')
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=128)
print loss_and_metrics