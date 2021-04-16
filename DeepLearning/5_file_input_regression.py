import tensorflow as tf
import numpy as np

# csv 파일을 불러와 데이터 파싱
xy = np.loadtxt('data-01-test-score.csv', delimiter=",", dtype=np.float32)

# 2차원 numpy 배열의 slicing
# xy[필요한 행 범위, 필요한 열 범위]
x_data = xy[:, 0:-1]    # 행은 전체, 열은 마지막 열 빼고
y_data = xy[:, [-1]]    # 행은 전체, 열은 마지막 열만

# 데이터가 잘 slicing 되었는지 확인
print(x_data, "\nx_data shape:", x_data.shape)
print(y_data, "\ny_data shape:", y_data.shape)

# 이하 동일
tf.model = tf.keras.Sequential()

tf.model.add(tf.keras.layers.Dense(units=1, input_dim=3))
tf.model.add(tf.keras.layers.Activation('linear'))

tf.model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=1e-5))
tf.model.summary()
history = tf.model.fit(x_data, y_data, epochs=100)

