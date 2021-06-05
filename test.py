import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1,2,3])
y_data = np.array([2,4,6])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1, ))
])
model.
