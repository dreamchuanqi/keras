#!/usr/bin/env python3

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt


def main():
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (
        test_images, test_labels) = fashion_mnist.load_data()
    print(train_images.shape)
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    print(class_names)
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=10)
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('\nTest accuracy:', test_acc)
    predictions = model.predict(test_images)
    print(predictions[0])
    print(np.argmax(predictions[0]), test_labels[0])
    print('=' * 60)


if __name__ == '__main__':
    main()
