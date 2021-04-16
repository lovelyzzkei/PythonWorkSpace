import numpy as np
import tensorflow as tf
import random

# 데이터 준비
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)

# 데이터 normalization
x_train, x_test = x_train / 255, x_test / 255  
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)  # color: black/white
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# y값들은 one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# hyper parameter 설정
learning_rate = 0.001
training_epochs = 12
batch_size = 128 

# 모델 설정
tf.model = tf.keras.Sequential()

# 첫 번째 layer: conv
tf.model.add(tf.keras.layers.Conv2D(filters=16, kernel_size=(3,3), input_shape=(28, 28, 1), activation='relu'))
tf.model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

# 두 번째 layer: conv
tf.model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), input_shape=(28, 28, 1), activation='relu'))
tf.model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

# 세 번째 layer: fully connected
tf.model.add(tf.keras.layers.Flatten())
tf.model.add(tf.keras.layers.Dense(units=10, kernel_initializer='glorot_normal', activation='softmax'))

tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=learning_rate), metrics=['accuracy'])
tf.model.summary()

tf.model.fit(x_train, y_train, epochs=training_epochs, batch_size=batch_size)

# predict 10 random hand-writing data
y_predicted = tf.model.predict(x_test)
for x in range(0, 10):
    random_index = random.randint(0, x_test.shape[0]-1)
    print("index: ", random_index,
          "actual y: ", np.argmax(y_test[random_index]),
          "predicted y: ", np.argmax(y_predicted[random_index]))

evaluation = tf.model.evaluate(x_test, y_test)
print('loss: ', evaluation[0])
print('accuracy', evaluation[1])