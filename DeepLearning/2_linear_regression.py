# 그래프를 build
# 그래프를 실행
# update variables and find graph

import tensorflow as tf
import numpy as np

x_train = [1,2,3]
y_train = [1,2,3]

# x,y 데이터를 학습시킬 모델 하나를 설정
# unit: 출력값의 dimension, input_dim: 입력값의 dimension
tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=1))    

# Cost를 minimize 시켜주는 방법: GradientDescent(경사하강)
# cost function: mse(mean-square-error)
# SGD: Standard Gradient Descendent, lr: learning rate
sgd = tf.keras.optimizers.SGD(lr=0.1)
tf.model.compile(loss='mse',optimizer=sgd) 

# prints summarty of the model to the terminal
tf.model.summary()

# fit() executes training
tf.model.fit(x_train, y_train, epochs=200)

# predict() returns predicted value
y_predict = tf.model.predict(np.array([5]))
print(y_predict)

