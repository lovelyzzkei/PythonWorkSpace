'''
Sequential API와 Functional API의 차이점
Sequential API: 직관적이고 편리하지만 복잡한 신경망을 구축할 수 없음
Functional API: 각 층을 일종의 함수로서 정의. 
'''

# Sequential API
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

# model = Sequential()
# model.add(Dense(3, input_dim=4, activation='softmax'))

# Functional API

from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers

inputs = Input(shape=(10,))                     # 10개의 입력을 받은 입력층
hidden1 = Dense(64, activation='relu')(inputs)  # 이전 층을 다음 층 함수의 입력으로 사용, 연결해줌
hidden2 = Dense(64, activation='relu')(hidden1)
output = Dense(1, activation='sigmoid')(hidden2)

model = Model(inputs=inputs, outputs=output)    # Model()에 입력과 출력 정의

# 앞에서 공부했던 선형 회귀를 Functional API로 구현

X = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 공부하는 시간
y = [11, 22, 33, 44, 53, 66, 77, 87, 95] # 각 공부하는 시간에 맵핑되는 성적

inputs = Input(shape=(1,))
x = Dense(1, activation='linear')(inputs)

model = Model(inputs=inputs, outputs=x)
model.compile(optimizer=optimizers.SGD, loss='mse', metrics=['accuracy'])
model.fit(X, y, batch_size=1, epochs=200)

# 로지스틱 회귀를 Functional API로 구현
import numpy as np

X = np.array([-50, -40, -30, -20, -10, -5, 0, 5, 10, 20, 30, 40, 50])
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) #숫자 10부터 1

inputs = Input(shape=(1,))
output = Dense(1, activation='sigmoid')(inputs)

model = Model(inputs=inputs, outputs=output)

# 다중 입력도 가능
from tensorflow.keras.layers import Input, Dense, concatenate
from tensorflow.keras.models import Model

# 두 개의 입력층 정의
inputA = Input(shape=(64,))
inputB = Input(shape=(128,))

# 첫 번째 입력층으로부터 분기되어 진행되는 인공 신경망 정의
x = Dense(16, activation='relu')(inputA)
x = Dense(8, activation='relu')(x)
x = Model(inputs=inputA, outputs=x)


# 두 번째 입력층으로부터 분기되어 진행되는 인공 신경망 정의
y = Dense(64, activation='relu')(inputB)
y = Dense(32, activation='relu')(y)
y = Dense(8, activation='relu')(y)
y = Model(inputs=inputB, outputs=y)

# 두 개의 인공 신경망의 출력을 연결
result = concatenate([x.output, y.output])

# 연결된 값을 입력으로 받는 밀집층 추가(Dense layer)
z = Dense(2, activation='relu')(result)

# 선형 회귀를 위해 linear로 설정
z = Dense(1, activation='linear')(z)

# 두 개의 입력층으로부터 분기되어 진행된 후 마지막에는 하나의 출력을 예측하는 모델
model = Model(inputs=[x.input, y.input], outputs=z)