'''
ONE-HOT ENCODING
단어집합(Vocabulary): 서로 다른 단어들의 집합이며 같은 단어의 변형 형태도 다른 단어로 간주 ex) book != books
단어 집합 생성 -> 단어 집합에 정수 인코딩 진행 -> 이를 벡터로 변환하는 작업이 ONE-HOT ENCODING

단어 집합의 크기를 벡터의 차원으로 하고, 표현하고 싶은 단어의 인덱스에 1의 값을 부여하고, 
다른 인덱스에는 0을 부여하는 벡터 표현 방식

ex) '나는 자연어 처리를 배운다'
    => ['나', '는', '자연어', '처리', '를', '배운다'] (형태학적 파싱으로 토큰화)
    => {'나': 0, '는': 1, '자연어': 2, '처리': 3, '를': 4, '배운다': 5}     (각 토큰에 대해 정수 인코딩)
    => [[1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1]
    ]

단점)
1. 단어 집합이 커질 수록 벡터를 저장하기 위해 필요한 공간도 계속 늘어남. => 비효율적일 수 있음
2. 단어의 유사도를 표현하지 못함. => 검색 시스템에서 관련 검색어를 보여줄 수 없음 
    => 단어의 잠재 의미를 반영하여 다차원 공간에 벡터화하는 방법으로 문제 해결
'''

# 한국어 문장의 원-핫 인코딩
from konlpy.tag import Okt

okt = Okt()
token = okt.morphs("나는 자연어 처리를 배운다") # ['나', '는', '자연어', '처리', '를', '배운다']

word2index = {}
for voca in token:
    if voca not in word2index.keys():
        word2index[voca] = len(word2index)  # {'나': 0, '는': 1, '자연어': 2, '처리': 3, '를': 4, '배운다': 5}

# 원-핫 인코딩 함수
def one_hot_encoding(word, word2index):
    one_hot_vector = [0]*len(word2index)
    index = word2index[word]
    one_hot_vector[index] = 1
    return one_hot_vector

one_hot_encoding('자연어', word2index)      # [0, 0, 1, 0, 0, 0]

##################################################################
# Keras에 존재하는 원-핫 인코딩 내장함수

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

text="나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

t = Tokenizer()         # 빈도수 기준으로 정수 인코딩
t.fit_on_texts([text])  # {'갈래': 1, '점심': 2, '햄버거': 3, '나랑': 4, '먹으러': 5, '메뉴는': 6, '최고야': 7}

encoded = t.texts_to_sequences([text])  # 부여한 정수 인덱스로 문장 인코딩
one_hot = to_categorical(encoded)

#[[[0. 0. 0. 0. 1. 0. 0. 0.]
#   [0. 0. 1. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 1. 0. 0.]
#   [0. 1. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 1. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 1. 0.]
#   [0. 0. 0. 1. 0. 0. 0. 0.]
#   [0. 1. 0. 0. 0. 0. 0. 0.]
#   [0. 1. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 1. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 1.]]]
