'''
LSA 실습
: 20개의 다른 주제를 가진 뉴스그룹 데이터를 가지고 문서의 수를 원하는 토픽의 수로 압축한 뒤
각 토픽당 가장 중요한 단어 5개를 출력하는 실습
'''

import re
import pandas as pd 
from nltk.corpus import stopwords
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
documents = dataset.data    # 11314개

# 텍스트 전처리
# 구두점, 숫자, 특수문자, 길이가 짧은 단어 제거
news_df = pd.DataFrame({'document':documents})

# 문자들만 남김 -> 정규 표현식 이용
news_df['clean_doc'] = news_df['document'].apply(lambda x: re.sub("[^a-zA-Z]", " ", x))

# pandas 객체의 열 혹은 행에 대해 함수를 적용하게 해주는 메서드
# document 열에 있는 각 문장들에 대해 길이가 3 이하인 단어들은 제거
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))

# 대, 소문자 통합
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: x.lower())

# 불용어 제거
stop_words = stopwords.words('english')     # 불용어들이 리스트 안에 정의되어 있음

tokenized_doc = news_df['clean_doc'].apply(lambda x: x.split()) # 토큰화 후
tokenized_doc = tokenized_doc.apply(lambda x: [w for w in x if w not in stop_words])    # 불용어 제거

# TF-IDF 행렬 만드는 작업 수행
# TfidfVectorizer()는 텍스트 데이터를 입력으로 받기 때문에 위 작업을 역으로 되돌리는 역 토큰화 작업 필요
detokenized_doc = []
for i in range(len(news_df)):
    t = ' '.join(tokenized_doc[i])  # 단어들을 
    detokenized_doc.append(t)

news_df['clean_doc'] = detokenized_doc

# TF-IDF 행렬 생성
vectorizer = TfidfVectorizer(stop_words='english',
                             max_features= 1000,     # 상위 단어 1000개만 가지고 만듦
                             max_df=0.5,
                             smooth_idf=True)

X = vectorizer.fit_transform(news_df['clean_doc'])  # (11314, 1000)

# 모든 전처리 완료!
# 토픽 모델링 시작
# 절단된 SVD을 이용해 다수의 행렬로 분해
# 주제는 20개
svd_model = TruncatedSVD(n_components=20, 
                        algorithm='randomized', # 무작위로 SVD 반환
                        n_iter=100, 
                        random_state=122)

svd_model.fit(X)
topic = svd_model.components_

terms = vectorizer.get_feature_names()  # 단어 집합 불러옴

# VT의 각 열은 토픽을 표현하기 위해 수치화된 각각의 단어 벡터들 
def get_topics(components, feature_names, n=5):
    for idx, topic in enumerate(components):
         
        # argsort(): 넘파이 배열의 원소를 오름차순으로 정렬하며 그 인덱스 값을 반환함
        # argsort()[:-n-1:-1]: 각각의 행은 주제를 나타내므로 그 주제를 가장 잘 나타내는
        # 상위 5개의 원소만을 출력  
        print("Topic {}:".format(idx+1), 
            [(feature_names[i], topic[i].round(5)) for i in topic.argsort()[:-n-1:-1]])


print(get_topics(svd_model.components_, terms))

