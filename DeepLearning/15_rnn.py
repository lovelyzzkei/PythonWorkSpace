import numpy as np
import tensorflow as tf

# 컴퓨터에 'hihell'을 주면 'ihello'가 나오도록 훈련
idx2char = ['h', 'i', 'e', 'l', 'o']

# one-hot encoding을 위하여 인덱스로 넘김
x_data = [[0, 1, 0, 2, 3, 3]]
y_data = [[1, 0, 2, 3, 3, 4]]

num_classes = 5
input_dim = 5           # 출력 one-hot의 크기와 동일
sequence_length = 6     # sequence 데이터의 크기 == x_data의 길이
learning_rate = 0.1

# 두 데이터 모두 one-hot encoding
x_one_hot = tf.keras.utils.to_categorical(x_data, num_classes=num_classes, dtype=np.float32)
y_one_hot = tf.keras.utils.to_categorical(y_data, num_classes=num_classes)

print(x_one_hot.shape)

tf.model = tf.keras.Sequential()

# RNN Cell을 만들고 RNN layer에 더함
# input_shape: x_one_hot의 shape이 (1, 6, 5) == (batch_size, sequence_length, input_dim)
cell = tf.keras.layers.LSTMCell(units=num_classes, input_shape=(sequence_length, input_dim))
tf.model.add(tf.keras.layers.RNN(cell=cell, return_sequences=True))

# Fully-Connected Layer
# TimeDistributed: 각 time에서 출력된 output을 내부에 선언해준 레이어와 연결시켜주는 역할을 함
# 입력값이 RNN을 한번 돌 때마다 나오는 output을 모두 softmax 레이어와 연결시킴
tf.model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(units=num_classes, activation='softmax')))
tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate), metrics=['accuracy'])

tf.model.fit(x_one_hot, y_one_hot, epochs=50)
tf.model.summary()

predictions = tf.model.predict(x_one_hot)
for i, prediction in enumerate(predictions):
    print(prediction)
    # print char using argmax, dict
    result_str = [idx2char[c] for c in np.argmax(prediction, axis=1)]
    print("\tPrediction str: ", ''.join(result_str))