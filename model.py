import tensorflow as tf
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard
import time



class BackgammonModel:

    def __init__(self, numberOfInputs, numberOfOutputs, epochs, batchSize): # epoch and batch size 1000 data point batch 1 and epoch 10 it will everysingle data point will be updated 10 times batch size is
        self.epochs = epochs
        self.batchSize = batchSize
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=(numberOfInputs,))) # maybe increase the layers
        self.model.add(Dense(128, activation='relu')) # below 0 return 0 else return x
        # dropout layer 25% 75% through 0.05 dropout
        self.model.add(Dropout(0.05))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.05))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy']) #changed from rmsprop




    def train(self, dataset):
        tensorboard = TensorBoard(log_dir="logs/{}".format(time.time()))
        input = []
        output = []
        for data in dataset:
            output.append(data[0])
            input.append(data[1])
        x = np.array(input).reshape((-1, self.numberOfInputs))
        y = to_categorical(output, num_classes=3)
        # Train and test data split
        boundary = int(0.8 * len(x))
        x_train = x[:boundary]
        x_test = x[boundary:]
        y_train = y[:boundary]
        y_test = y[boundary:]
        history = self.model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=self.epochs,
                       batch_size=self.batchSize, callbacks=[tensorboard])
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')
        plt.show()

        # Plot the training and validation loss over the epochs
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')
        plt.show()
    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs),verbose=None)[0][index]


    def save(self,filepath):
        self.model.save(filepath)

    def update_internal_model(self,nn):
        self.model = nn

    def summary(self):
        return self.model.summary()
