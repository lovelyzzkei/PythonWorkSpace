import numpy as np
import tensorflow as tf

sentence = ("if you want to build a ship, don't drum up people together to "
            "collect wood and don't assign them tasks and work, but rather "
            "teach them to long for the endless immensity of the sea.")

char_set = list(set(sentence))
char_dic = {c: i for i, c in enumerate(char_set)}

# hyper parameter
data_dim = len(char_set)
hidden_size = len(char_set)
num_classes = len(char_set)
sequence_length = 10    # 임의의 값
learning_rate = 0.1

# 문장이 길기 때문에 일정 길이로 잘라서 처리
dataX = []
dataY = []
for i in range(0, len(sentence) - sequence_length):
    x_str = sentence[i:i+sequence_length]
    y_str = sentence[i + 1 : i + sequence_length + 1]
    print(i, x_str, '->', y_str) 

    x = [char_dic[c] for c in x_str]
    y = [char_dic[c] for c in y_str]

    dataX.append(x)
    dataY.append(y)

batch_size = len(dataX)

# 데이터 one-hot encoding화
x_one_hot = tf.keras.utils.to_categorical(dataX, num_classes)
y_one_hot = tf.keras.utils.to_categorical(dataY, num_classes)

print(x_one_hot.shape) # (170, 10, 25)

# 모델 설정
# LSTM layer 두개 설정 -> stacked RNN
tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.LSTM(units=num_classes, input_shape=(sequence_length, x_one_hot.shape[2]), return_sequences=True))
tf.model.add(tf.keras.layers.LSTM(units=num_classes, return_sequences=True))
tf.model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(units=num_classes, activation='softmax')))
tf.model.summary()
tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=learning_rate), metrics=['accuracy'])
tf.model.fit(x_one_hot, y_one_hot, epochs=100)

# 테스팅
results = tf.model.predict(x_one_hot)
for j, result in enumerate(results):
    index = np.argmax(result, axis=1)
    if j == 0:  # print all for the first result to make a sentence
        print(''.join([char_set[t] for t in index]), end='')
    else:
        print(char_set[index[-1]], end='')