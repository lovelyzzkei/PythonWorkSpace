import numpy as np
import tensorflow as tf

sample = "if you want you"  
idx2char = list(set(sample))                        # idx -> char
char2idx = {c: i for i, c in enumerate(idx2char)}   # char -> idx

# hyper parameter 설정
dic_size = len(char2idx)        # 사용하는 문자의 개수
hidden_size = len(char2idx)     # RNN의 output size
num_classes = len(char2idx)     # 출력값의 문자의 개수
batch_size = 1
sequence_data = len(sample) -1  # 입력값의 길이
learning_rate = 0.1

# sample 문자열을 인덱싱 -> x, y 데이터 준비
sample_idx = [char2idx[c] for c in sample]  
x_data = [sample_idx[:-1]]
y_data = [sample_idx[1:]]

# x, y 데이터 one-hot encoding
x_one_hot = tf.keras.utils.to_categorical(x_data, num_classes)
y_one_hot = tf.keras.utils.to_categorical(y_data, num_classes)

# 모델 설정
tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.LSTM(units=num_classes, input_shape=(sequence_data, dic_size), return_sequences=True))
tf.model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(units=num_classes, activation='softmax')))
tf.model.summary()

tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=learning_rate), metrics=['accuracy'])
tf.model.fit(x_one_hot, y_one_hot, epochs=50)

predictions = tf.model.predict(x_one_hot)
print(predictions)

for i, prediction in enumerate(predictions):
    result_str = [idx2char[c] for c in np.argmax(prediction, axis=1)]
    print(result_str)
    print("\tPrediction str: ", ''.join(result_str))