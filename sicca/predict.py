import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.preprocessing import image
import numpy as np


class Predictor:
    def __init__(self):
        # Import model architecture to recreate the network
        temp = keras.applications.vgg16.VGG16()
        self.model = Sequential()
        for layer in temp.layers[:-1]:
            self.model.add(layer)
        for layer in self.model.layers:
            layer.trainable = False
        self.model.add(Dense(1, activation='sigmoid'))
        # Load pre trained weights into model skeleton
        self.model.load_weights('head_tail.h5')

    @staticmethod
    def load_img(path):
        """Return the image loaded and transformed into suitable format for the model to predict"""
        img = image.load_img(path, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        return img

    def predict(self, img_path):
        """Returns string representation of the prediction made on the input image"""
        img = self.load_img(img_path)
        pred = self.model.predict_classes(img)  # 0: Heads, 1: Tails
        if pred[0][0] == 0:
            res = 'Heads'
        else:
            res = 'Tails'
        return res
