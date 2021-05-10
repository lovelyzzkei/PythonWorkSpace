import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN, LSTM, Bidirectional

train_X = [[[0.1, 4.2, 1.5, 1.1, 2.8], 
           [1.0, 3.1, 2.5, 0.7, 1.1], 
           [0.3, 2.1, 1.5, 2.1, 0.1], 
           [2.2, 1.4, 0.5, 0.9, 1.1]]]   # 2D 텐서

train_X = np.array(train_X, dtype=np.float32)   # 3D 텐서로 변경

# simpleRNN 구현
rnn = SimpleRNN(3, return_sequences=False, return_state=True)
hidden_state = rnn(train_X)

print(hidden_state, hidden_state[0].shape)

# return_sequence=True: -> 모든 시점에서 값 반환
# return_state=True: -> return_sequence의 값의 여부와 상관없이 마지막 시점의 은닉상태 출력

# LSTM 구현
# return_state=True일 경우 마지막 cell state까지 해서 3개의 값 반환

lstm = LSTM(3, return_sequences=False, return_state=True)
hidden_state, last_state, last_cell_state = lstm(train_X)

print(hidden_state, hidden_state.shape)
print(last_state, last_state.shape)
print(last_cell_state, last_cell_state.shape)
