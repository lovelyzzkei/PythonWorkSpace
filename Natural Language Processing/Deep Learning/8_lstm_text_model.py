import pandas as pd
import numpy as np
from string import punctuation  # 데이터 전처리를 위해 import
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical


# 데이터에 대한 이해
# len(df): 1324
# 열 개수(특성 개수): 15. 이 중 사용할 열은 'headline'
# NULL 값은 없음. 대신 Unknown 값이 존재. -> 노이즈 데이터에 대한 정제 작업 필요

df = pd.read_csv('ArticlesApril2018.csv')
print(df['headline'].values)    # 리스트 형태

# 필요한 headline 열만 따로 추출
headline = []
headline.extend(df['headline'].values)

# Unknown 제거: 1324 -> 1214 로 감소
headline = [i for i in headline if i != 'Unknown']

# 데이터 전처리 수행
# 구두점 제거 및 소문자화
def repreprocessing(s):
    s = s.encode("utf8").decode("ascii",'ignore')

    # 구두점 제거와 소문자화 동시에
    return ''.join(c for c in s if c not in punctuation).lower()

text = [repreprocessing(x) for x in headline]

# 데이터 전처리 끝. 단어 토큰화 및 단어 집합 생성
# 총 3494개의 단어 존재
t = Tokenizer()
t.fit_on_texts(text)
vocab_size = len(t.word_index) + 1

# 정수 인코딩 및 문장 분해
sequences = list()

for line in text:
    encoded = t.texts_to_sequences([line])[0]
    for i in range(1, len(encoded)):
        sequence = encoded[:i+1]
        sequences.append(sequence)

# 인덱스로 단어를 참고하기 위한 idx2word 생성
idx2word = {}
for key, value in t.word_index.items():
    idx2word[value] = key

# 모든 문장의 길이를 맞추기 위한 패딩 작업
max_len = max(len(l) for l in sequences)
sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')

# 훈련 데이터와 레이블 분리
sequences = np.array(sequences)
X = sequences[:, :-1]
y = sequences[:,-1]

# 레이블 원-핫 인코딩 처리
y = to_categorical(y, num_classes=vocab_size)

# 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM

model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
model.add(LSTM(128))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=2)

# 문장 생성 함수
def sentence_generation(model, t, current_word, n):
    init_word = current_word
    sentence = ''
    for _ in range(n):
        encoded = t.texts_to_sequences([current_word])[0]
        encoded = pad_sequences([encoded], maxlen=23, padding='pre')
        result = model.predict_classes(encoded, verbose=0)

        for word, index in t.word_index.items():
            if index == result:
                break
        current_word= current_word + ' ' + word
        sentence = sentence + ' ' + word
    
    sentence = init_word + sentence
    return sentence

print(sentence_generation(model, t, 'how', 10))