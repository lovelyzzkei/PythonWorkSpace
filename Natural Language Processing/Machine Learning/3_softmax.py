import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

'''
데이터 준비
150개의 샘플, 6개의 열(특성)
첫 열은 ID, 마지막 열은 품종, 나머지 4개의 열이 데이터의 특성
품종은 세종류
샘플 데이터의 4개의 특성으로부터 3개 중 어떤 품종인지를 예측하는 문제
'''
data = pd.read_csv("IRIS.csv", encoding='latin1')

# 각각의 품종에 정수 인코딩을 수행
data['species'] = data['species'].replace(['Iris-virginica','Iris-setosa','Iris-versicolor'], [0,1,2])

# 특성과 품종을 분리 (독립변수와 종속변수 분리)
data_X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
data_y = data['species'].values
print(data_y[:5])
# 훈련 데이터, 테스트 데이터 8:2로 분리 및 종속변수 원-핫 인코딩
(X_train, X_test, y_train, y_test) = train_test_split(data_X, data_y, train_size=0.8, random_state=1)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 소프트맥스 회귀 모델링
model = Sequential()
model.add(Dense(units=3, input_dim=4, activation='softmax'))
adam = optimizers.Adam(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
history = model.fit(X_train, y_train, batch_size=1, epochs=200, validation_data=(X_test, y_test))

print("\n 테스트 정확도: %.4f" % (model.evaluate(X_test, y_test)[1]))