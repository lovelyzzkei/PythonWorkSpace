import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

x_train = [1,2,3]
y_train = [1,2,3]

W = tf.Variable(tf.random_normal([1]), name='weight')
X = tf.constant