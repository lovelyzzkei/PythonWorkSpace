# 텍스트 전처리
# Tokenizer(): 토큰화와 정수 인코딩
# fit_on_texts(): 코퍼스 데이터를 가지고 빈도수 기준으로 단어 집합을 생성

from tensorflow.keras.preprocessing.text import Tokenizer

t = Tokenizer()

fit_text = "The earth is an awesome place is live"
t.fit_on_texts([fit_text])  

test_text = "The earth is an great place live"

# test_text를 미리 정수 인코딩한 단어 집합을 가지고 정수 인코딩
sequences = t.texts_to_sequences([test_text])[0]  

print("sequences: ", sequences)
print(t.word_index)

# pad_sequence(): 패딩, 모든 샘플의 길이를 동일하게 맞추어야할 때 사용
from tensorflow.keras.preprocessing.sequence import pad_sequences

pad_sequences([[1,2,3],[3,4,5,6],[7,8]], 
                maxlen=3,           # 길이 3으로 패딩
                padding='pre')      # 길이가 모자란 샘플들은 '앞'에 0을 채움, 길이가 길면 앞에서 자름


# 워드 임베딩(Word Embedding)
# : 텍스트 내의 단어들을 밀집 벡터(Dense vector)로 만드는 것
# 원-핫 벡터와 대조적으로 저차원이며, 훈련 데이터로부터 학습을 하고, 값이 실수인 벡터
# ex) [0.1, -0.2, 0.8, 1.2]
# 인공 신경망의 가중치가 학습되는 방법과 같은 방식으로 값이 학습되며 변경됨.

# Embedding(단어집합의 크기, 임베딩 한 후 벡터의 크기, 각 입력 시퀀스의 길이): 
# 단어를 밀집 벡터로 만듦. 정수 인코딩이 된 단어들을 입력으로 받아서 입력 수행.
# 인공 신경망에서 하나의 층을 이룸
# (num of samples, input_length)인 2D 정수 텐서를 입력 받음


# evaluate(): 테스트 데이터를 통해 학습한 모델의 정확도를 평가
# predict(): 임의의 입력에 대한 모델의 출력값 확인