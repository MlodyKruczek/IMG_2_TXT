# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import tensorflow as tf







def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)  # y labels are oh-encoded

    n_train = mnist.train.num_examples  # 55,000
    n_validation = mnist.validation.num_examples  # 5000
    n_test = mnist.test.num_examples  # 10,000

    n_input = 784  # input layer (28x28 pixels)
    n_hidden1 = 512  # 1st hidden layer
    n_hidden2 = 256  # 2nd hidden layer
    n_hidden3 = 128  # 3rd hidden layer
    n_output = 10  # output layer (0-9 digits)

    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])



# Press the green button in the guttennr to run the script.
if __name__ == '__main__':
    print_hi('PyCharm2')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
