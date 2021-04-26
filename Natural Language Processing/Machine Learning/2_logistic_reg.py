import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

# 일정 크기 이상의 수에는 1을, 이하의 수에는 0을 맵핑
X = np.array([-50, -40, -30, -20, -10, -5, 0, 5, 10, 20, 30, 40, 50])
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) #숫자 0부터 1

model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))

sgd = optimizers.SGD(lr=0.01)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['binary_accuracy'])

model.fit(X, y, batch_size=1, epochs=200, shuffle=False)

print(model.predict([1, 2, 3, 4, 5]))