import numpy as np
import theano
import keras

from keras.datasets import cifar10
from keras.models  import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Convolution3D, MaxPooling3D
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.models  import Sequential
import matplotlib.pyplot as plt
#from keras.models import load_model


#learning parameter  for SGD

batchSize = 50                    #-- Training Batch Size
num_epochs = 1000                   #-- Number of epochs for training   
learningRate= 0.001               #-- Learning rate for the network
lr_weight_decay = 0.95            #-- Learning weight decay. Reduce the learn rate by 0.95 after epoch



img_rows, img_cols = 32, 32

#uilding  model
model = Sequential()


model.add(Convolution3D(12,3,3,3,activation='linear',border_mode='valid',input_shape=(1,7,img_rows, img_cols)))
model.add(Convolution3D(24,1,3,3,activation='linear',border_mode='valid'))
model.add(MaxPooling3D(pool_size=(1,2, 2)))
model.add(Convolution3D(48,3,3,3,activation='linear',border_mode='valid'))
model.add(MaxPooling3D(pool_size=(1,2, 2)))
model.add(Convolution3D(64,3,3,3,activation='linear',border_mode='valid'))
#model.add(Convolution3D(128,1,4,4,activation='linear',border_mode='valid'))

model.add(Flatten())
model.add(Dense(128))


#model.add(Flatten())
model.add(Dense(2))
model.add(Activation('softmax'))

model.summary()

sgd = SGD(lr=learningRate, decay = lr_weight_decay)
#model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
model.compile(loss='mean_squared_error',optimizer='Adam',metrics=['accuracy'])



X_train=np.load("in1.npy")
Y_train=np.load("out1.npy")
#history = model.fit(X_train, Y_train, batch_size=batchSize, nb_epoch=num_epochs, verbose=1, shuffle=True, validation_data=(X_test, Y_test))
history = model.fit(X_train, Y_train, batch_size=batchSize, nb_epoch=num_epochs, verbose=1, shuffle=True, validation_data=(X_train, Y_train))




#model.save('my_model.h5')




