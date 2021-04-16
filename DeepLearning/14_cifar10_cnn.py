import tensorflow as tf
import numpy as np
import random

# cifar10의 이미지 데이터 준비
cifar = tf.keras.datasets.cifar10
(x_train, y_train), (x_test, y_test) = cifar.load_data()

# 데이터 개수 확인. 훈련 데이터: 50000개, 테스트 데이터: 10000개
print(len(x_train), len(x_test))

# 데이터 형태 확인
print(x_train.shape)    # (50000, 32, 32, 3) 

# 데이터 전처리: normalization, one-hot encoding
x_train , x_test = x_train / 255, x_test / 255 
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# hyper parameter 설정
drop_rate = 0.2
epochs = 10
batch_size = 5

# 모델 설정
tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), input_shape=(32, 32, 3), activation='relu'))
tf.model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
tf.model.add(tf.keras.layers.Dropout(drop_rate))

tf.model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), input_shape=(32, 32, 3), activation='relu'))
tf.model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
tf.model.add(tf.keras.layers.Dropout(drop_rate))

tf.model.add(tf.keras.layers.Flatten())
tf.model.add(tf.keras.layers.Dense(units=10, kernel_initializer='glorot_normal', activation='softmax'))

tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])
tf.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

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