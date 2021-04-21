'''
BOW: 단어들의 출현 빈도(frequency)에만 집중하는 텍스트 데이터의 수치화 표현 방법
각 단어에 고유한 정수 인덱스를 부여하고,
각 인덱스의 위치에 단어 토큰의 등장 횟수를 기록한 벡터를 만듦
-> 텍스트 내에 어떤 단어들이 중요한지를 보고싶다
'''

from konlpy.tag import Okt
import re

okt = Okt()
token = re.sub("(\.)", "", "정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.")  # 정제: 마침표 모두 제거
token = okt.morphs(token)   # 단어 토큰화

# 단어 집합 생성
word2index = {}
bow = []
for voca in token:
    # 각 단어에 고유한 정수 인덱스 부여
    if voca not in word2index.keys():
        word2index[voca] = len(word2index)  
        bow.insert(len(word2index)-1, 1)    # 각 인덱스의 위치에 단어 토큰의 등장 횟수를 기록한 벡터 만듦
    
    else:
        index = word2index[voca]
        bow[index] += 1


print(word2index)
print(bow)

####################################################
# 사이킷런으로 BoW 만들기
from sklearn.feature_extraction.text import CountVectorizer

corpus = ["You know I love you."]
vector = CountVectorizer()

# fit_transform(): 주어진 코퍼스 데이터를 단어 토큰화
print(vector.fit_transform(corpus).toarray())
print(vector.vocabulary_)