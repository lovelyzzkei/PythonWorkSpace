import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.python.training import optimizer

# 20개의 다른 주제를 가진 18,846개의 뉴스 그룹 이메일 데이터. 그 중에서 훈련 데이터를 가져옴
newsdata = fetch_20newsgroups(subset='train')

print(newsdata.keys())  # dict_keys(['data', 'filenames', 'target_names', 'target', 'DESCR'])

print(newsdata.target[0])
print(newsdata.target_names[0])

# 이번 실습의 목적은 테스트 데이터에서 이메일 본문을 보고 20개의 주제 중 어떤 주제인지를 맞추는 것.
# 'target_names'에는 20개의 주제의 이름들이 있으며 'target'은 이 주제를 0~19까지 맵핑한 수들.
# 그러면 입력 데이터는 'data'가 되어야 하며 출력 데이터는 'target'이 되면 좋을듯 하다.

# print(newsdata.data[0])

# 뉴스그룹 데이터와 target을 데이터프레임으로 만들어 데이터에 대해 더 깊게 분석
data = pd.DataFrame(data=newsdata.data, columns=['email'])
data['target'] = pd.Series(newsdata.target) # 데이터프레임에 'target'열 추가
print(data[:5])

# Null 값의 샘플이 있는지 확인
print(data.isnull().values.any())

# nunique()를 통해 샘플 중 중복을 제거한 개수 확인
print(data['email'].nunique())
print(data['target'].nunique())

# 각 레이블들의 분포 확인. 각 레이블마다 약 500~600개 정도의 데이터들 존재
print(data.groupby('target').size().reset_index(name='count'))

# 훈련 데이터와 테스트 데이터 설정
newsdata_test = fetch_20newsgroups(subset='test', shuffle=True)

train_email = data['email']
train_label = data['target']
test_email = newsdata_test.data
test_label = newsdata_test.target

# 텍스트 전처리 수행
max_words = 10000   # 실습에 사용할 단어의 최대 개수
num_classes = 20    # 레이블의 수

# 전처리 함수
def prepare_data(train_data, test_data, mode):
    t = Tokenizer(num_words=max_words)
    t.fit_on_texts(train_data)  # 빈도수 기준으로 단어 집합 생성
    X_train = t.texts_to_matrix(train_data, mode=mode)
    X_test = t.texts_to_matrix(test_data, mode=mode)

    return X_train, X_test, t.index_word

X_train, X_test, index_to_word = prepare_data(train_email, test_email, 'binary')
y_train = to_categorical(train_label, num_classes)  # 레이블 원-핫 인코딩
y_test = to_categorical(test_label, num_classes)


# 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

def fit_and_evaluate(X_train, y_train, X_test, y_test):
    model = Sequential()
    model.add(Dense(256, input_shape=(max_words,), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax')) # 다중 클래스 분류-> 소프트맥스 사용

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, batch_size=128, epochs=5, validation_split=0.1)

    score = model.evaluate(X_test, y_test, batch_size=128)
    
    return score[1]

# texts_to_matrix() 4개의 모든 모드에 대하여 결과 확인
modes = ['binary', 'count', 'freq', 'tfidf']

for mode in modes:
    X_train, X_test, _ = prepare_data(train_email, test_email, mode)
    score = fit_and_evaluate(X_train, y_train, X_test, y_test)
    print(mode,":", score)