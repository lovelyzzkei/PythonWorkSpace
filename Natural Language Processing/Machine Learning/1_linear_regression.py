'''
케라스를 이용하여 Linear Regression 구현
1. Sequential()로 모델을 만들고
2. add()를 통해 입력과 출력 벡터의 차원과 같은 필요한 정보들 추가
'''

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

X=[1,2,3,4,5,6,7,8,9] # 공부하는 시간
y=[11,22,33,44,53,66,77,87,95] # 각 공부하는 시간에 맵핑되는 성적

# 1. 모델 생성 
model = Sequential()

# 2. 모델에 필요한 정보들 추가
model.add(Dense(units=1,                # 입력값인 X의 차원
                input_dim=1,            # 출력값인 y의 차원
                activation='linear'))   # 사용할 함수. 선형회귀 -> linear

# 3. 오차 최적화 알고리즘 설정
sgd = optimizers.SGD(lr=0.01)

# 4. 모델에 비용함수를 엮어줌 (compile)
model.compile(optimizer=sgd,           # 최적화 알고리즘
              loss='mse',               # 비용함수
              metrics=['mse'])          # 모델을 평가할 값, 척도, 평가지표
                                        # 앞에서 얘기한 정밀도, 재현율 등이 여기에 속함

# 5. 학습 진행.
model.fit(X, y, 
          batch_size=1,         
          epochs=300,           # 오차 최소화 작업(훈련 횟수)을 300번 수행
          shuffle=False)

# 오차를 최소화하는 직선 시각화
plt.plot(X, model.predict(X), 'b', X, y, 'k.')
plt.show()

# predict(): 학습이 완료된 모델이 입력된 데이터에 대해서 어떤 값을 예측하는지 보여줌
print(model.predict([9.5]))