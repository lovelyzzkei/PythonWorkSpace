# XOR by wide NN
import tensorflow as tf
import numpy as np

x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)

# wide 하고 deep 할수록 값은 더 정확해진다(일반적)
tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(units=10, input_dim=2, activation='sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=10, activation='sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=10, activation='sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=10, activation='sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

tf.model.compile(loss='binary_crossentropy', optimizer=tf.optimizers.Adam(lr=0.1), metrics='accuracy')
tf.model.summary()

history = tf.model.fit(x_data, y_data, epochs=5000)

predictions = tf.model.predict(x_data)
print('Prediction: \n', predictions)

score = tf.model.evaluate(x_data, y_data)
print('Accuracy: ', score[1])

'''
Prediction: 
 [[6.3730351e-07]
 [9.9999863e-01]
 [9.9999857e-01]
 [6.1550827e-07]]
1/1 [==============================] - 0s 108ms/step - loss: 1.0333e-06 - accuracy: 1.0000
Accuracy:  1.0
'''
