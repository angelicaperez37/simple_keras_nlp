from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ReduceLROnPlateau, EarlyStopping

class SimpleNeuralNet:

    def __init__(self):
        self.model = self.createModel()

    def createModel(self):
        model = Sequential()
        model.add(Dense(32, input_shape=(2,)))
        model.add(Dense(32))
        model.add(Dense(1, activation='sigmoid'))
        print (model.summary())
        model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def trainModel(self, X_train, y_train):
        self.model.fit(x=X_train, y=y_train, epochs=15, verbose=1, callbacks=[ReduceLROnPlateau(), EarlyStopping(patience=3)], validation_split=0.2, shuffle=True)
