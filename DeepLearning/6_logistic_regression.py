import tensorflow as tf
import numpy as np

x_data = [[1, 2],
          [2, 3],
          [3, 1],
          [4, 3],
          [5, 3],
          [6, 2]]
y_data = [[0],
          [0],
          [0],
          [1],
          [1],
          [1]]


tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=2))

# sigmoid activation을 사용하여 logistic regression 구현
tf.model.add(tf.keras.layers.Activation('sigmoid'))

# keras내 구현되어 있는 binary classification의 cost function 사용
tf.model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.SGD(lr=0.01), metrics=['accuracy'])
tf.model.summary()

history = tf.model.fit(x_data, y_data, epochs=500)

print("Accuracy:", history.history['accuracy'][-1])
print(tf.model.predict(np.array([[7,3]])))
