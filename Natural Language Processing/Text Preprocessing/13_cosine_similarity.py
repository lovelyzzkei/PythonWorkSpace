'''
문서1: 저는 사과 좋아요
문서2: 저는 바나나 좋아요
문서3: 저는 바나나 좋아요 저는 바나나 좋아요

위 세문장에 대하여 코사인 유사도를 구하는 실습
'''

from numpy import dot
from numpy.linalg import norm
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


# 코사인 유사도를 구하는 함수 정의
# dot(): 내적 수행
# norm(): 벡터의 노름, 벡터의 크기를 계산하는 함수
# def cos_sim(A, B):
#     return dot(A, B) / (norm(A) * norm(B))

# corpus = ['저는 사과 좋아요', '저는 바나나 좋아요', '저는 바나나 좋아요 저는 바나나 좋아요']

# # 앞에서 배운 CountVectorizer()를 통해 DTM 생성
# vector = CountVectorizer()

# v1, v2, v3 = vector.fit_transform(corpus).toarray()
# print(v1, v2, v3)

# print(cos_sim(v1, v2))
# print(cos_sim(v1, v3))
# print(cos_sim(v2, v3))  # 1.00 => 빈도수가 높다고 유사도가 커지지 않음


############################################################################
# 영화 추천 시스템 만들기
# TF-IDF와 코사인 유사도 사용

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 처리할 데이터 확인
data = pd.read_csv('movies_metadata.csv', low_memory=False)
# print(data.head(2))

# title과 overview 정보만을 뽑아 좋아하는 영화를 입력하면
# 그 영화와 줄거리가 비슷한 영화들을 추천하는 시스템

# 20000개의 데이터만 사용
data = data.head(20000)
data['overview'] = data['overview'].fillna('')  # null 값들에 빈 값들을 넣어 null값 제거

# tf-idf 수행
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])    # 20000개의 영화에 대한 DTM 생성

# linear_kernel(): 코사인 유사도를 계산해줌
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
print(tfidf_matrix.shape)   # (20000, 47487) -> 20000개의 영화를 표현하는데 47487개의 단어 사용됨
print(cosine_sim.shape)     # (20000, 20000)

# 영화의 타이틀과 인덱스를 가진 테이블을 만듦. word2idx
# 시리즈: 1차원 배열의 값(values)에 각 값에 대응되는 인덱스(index)를 부여할 수 있는 클래스
# values=data.index, index=data['title'], drop_duplicates(): 중복 열 삭제
indices = pd.Series(data.index, index=data['title']).drop_duplicates()

# 영화 추천 시스템
def get_recommended(title):
    idx = indices[title]    # 해당 영화의 인덱스 가져옴
    sim_scores = list(enumerate(cosine_sim[idx]))   # 해당 영화와 다른 모든 영화와의 코사인 유사도 가져옴

    # 유사도에 따라 영화 정렬
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)

    # 상위 10개의 인덱스 가져옴. (0번째에는 자기 자신이 있기 때문에 제외)
    movie_indices = [i[0] for i in sim_scores[1:11]]

    # 10개의 제목 반환
    # iloc(): 시리즈에서 해당 인덱스에 위치한 데이터 반환
    return data['title'].iloc[movie_indices]

print(get_recommended('The Dark Knight Rises'))