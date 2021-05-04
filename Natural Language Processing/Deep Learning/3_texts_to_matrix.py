'''
다층 퍼셉트론으로 자연어 처리를 하는 실습
'''

# texts_to_matrix() 이해하기

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

texts = ['먹고 싶은 사과', '먹고 싶은 바나나', '길고 노란 바나나 바나나', '저는 과일이 좋아요']

t = Tokenizer()
t.fit_on_texts(texts)
print(t.word_index) #{'바나나': 1, '먹고': 2, '싶은': 3, '사과': 4, '길고': 5, '노란': 6, '저는': 7, '과일이': 8, '좋아요': 9}
print(t.index_word)

# texts_to_matrix(): 정수 인코딩 된 단어 집합을 가지고 DTM을 만듦.
# 첫 열에 있는 0은 아무 의미 없는 데이터
# count, binary, freq, tfidf 의 4가지 모드 지원
print(t.texts_to_matrix(texts, mode='count'))
#[[0. 0. 1. 1. 1. 0. 0. 0. 0. 0.]
# [0. 1. 1. 1. 0. 0. 0. 0. 0. 0.]
# [0. 2. 0. 0. 0. 1. 1. 0. 0. 0.]
# [0. 0. 0. 0. 0. 0. 0. 1. 1. 1.]]