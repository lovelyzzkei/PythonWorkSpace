'''
다대일 구조의 RNN을 사용하여 문맥을 반영해서 텍스트를 생성하는 모델
예를 들어, '그의 말이'가 입력으로 들어오면 '법이다'를 출력하는 모델
'''

# 데이터에 대한 이해와 전처리
from inspect import Parameter
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
import numpy as np

text="""경마장에 있는 말이 뛰고 있다\n
        그의 말이 법이다\n
        가는 말이 고와야 오는 말이 곱다\n"""

# 단어 집합 생성
t = Tokenizer()
t.fit_on_texts([text])

# 케라스 토크나이저의 정수 인코딩은 인덱스가 1부터 시작하지만,
# 케라스 원-핫 인코딩에서 배열의 인덱스가 0부터 시작하여 미리 1을 더해놓음
vocab_size = len(t.word_index) + 1

# 훈련 데이터 생성
# '그의 말이' -> [2, 3]
# 아직 레이블을 분리하지 않은 상태
sequences = list()

for line in text.split('\n'):
    encoded = t.texts_to_sequences([line])[0]
    for i in range(1, len(encoded)):
        sequence = encoded[:i+1]
        sequences.append(sequence)

# 패딩 작업을 위해 길이 일치
max_len = max(len(l) for l in sequences)
sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')

# 각 시퀀스의 마지막 단어를 레이블로 분리
sequences = np.array(sequences)
X = sequences[:, :-1]   # 마지막 값 제외하고 나머지
y = sequences[:, -1]    # 마지막 값만

# 레이블 원-핫 인코딩
y = to_categorical(y, num_classes=vocab_size)

# 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, SimpleRNN

model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
model.add(SimpleRNN(32))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=2)

# 모델이 정확하게 예측하고 있는지 문장을 생성하는 함수 생성
def sentence_generatioin(model, t, current_word, n):
    init_word = current_word
    sentence = ''
    for _ in range(n):
        encoded = t.texts_to_sequences([current_word])[0]
        encoded = pad_sequences([encoded], maxlen=5, padding='pre')
        result = model.predict_classes(encoded, verbose=0)

        for word, index in t.word_index.items():
            if index == result:
                break
        current_word = current_word + ' ' + word
        sentence = sentence + ' ' + word

    sentence = init_word + sentence
    return sentence 

print(sentence_generatioin(model, t, '가는', 6))
