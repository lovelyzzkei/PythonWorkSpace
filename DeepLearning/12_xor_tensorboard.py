# 깔끔하게 그래프로 그리기
import datetime
import numpy as np
import os
import tensorflow as tf

x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)

# 두 network를 합친 형태로 구현
# xor_wide_nn.py와 코드 동일
# 두 network를 합친 형태로 구현
tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(units=2, input_dim=2))   # layer 1
tf.model.add(tf.keras.layers.Activation('sigmoid'))
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=2))   # layer 2
tf.model.add(tf.keras.layers.Activation('sigmoid'))
tf.model.compile(loss='binary_crossentropy', optimizer=tf.optimizers.SGD(lr=0.01), metrics='accuracy')
tf.model.summary()

# callback 함수 만들어줌
log_dir = os.path.join(".", "logs", "fit", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# callback 함수를 fit()에 같이 넣어 학습시킴
history = tf.model.fit(x_data, y_data, epochs=5000, callbacks=[tensorboard_callback])

predictions = tf.model.predict(x_data)
print('Prediction: \n', predictions)

score = tf.model.evaluate(x_data, y_data)
print('Accuracy: ', score[1])
