import tensorflow
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
from keras.utils import to_categorical
import numpy as np


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
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy']) #changed from rmsprop

    def train(self, dataset):
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
        self.model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=self.epochs,
                       batch_size=self.batchSize) # define a NN that can take the right structure run occasionaly because it is super slow
        self.model.save(r'C:\Users\Max\PycharmProjects\BackgammonPy\Models\model_1')
    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]
