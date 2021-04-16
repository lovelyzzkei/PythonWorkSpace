import numpy as np
import tensorflow as tf

# 주어진 동물의 특징들을 가지고 그 동물이 무엇인지 예측하는 모델 학습
# 데이터의 형태
# hair, feathers, eggs, milk, airborne, aquatic, predator, ..., type(integer values in 0~6)
xy = np.loadtxt('data-04-zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

nb_classes = 7 # 0부터 6까지 7개의 종류

# 레이블을 넘겨줄 때는 One-hot Encoding 방식으로 넘겨주어야 함. 
# csv에서 불러온 data에 대한 변환 작업이 필요
y_one_hot = tf.keras.utils.to_categorical(y_data, nb_classes)
print("one_hot:", y_one_hot)

# 아래는 softmax classification과 동일
tf.model = tf.keras.Sequential()
tf.model.add(tf.keras.layers.Dense(units=nb_classes, input_dim=16, activation='softmax'))
tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.SGD(lr=0.1), metrics=['accuracy'])
# tf.model.summary()

history = tf.model.fit(x_data, y_one_hot, epochs=300)

# Single data test
test_data = np.array([[0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0]]) # expected prediction == 3 (feathers)
print(tf.model.predict(test_data), np.argmax(tf.model.predict(test_data), 1))

# Full x_data test
pred = np.argmax(tf.model.predict(x_data), 1)
for p, y in zip(pred, y_data.flatten()):
    print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))