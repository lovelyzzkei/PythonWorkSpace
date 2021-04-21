'''
DTM: 서로 다른 문서들의 BoW들을 결합한 표현 방법, Document-Term Matrix)
다수의 문서에서 등장하는 각 단어들의 빈도를 행렬로 표현한 것
각 문서에 대한 BoW를 하나의 행렬로 만든 것
문서들을 서로 비교할 수 있도록 수치화할 수 있음

한계점)
1. 희소 표현 (Sparse representation)
원-핫 인코딩과 마찬가지로 패딩값(0인 값의 부분, 희소 벡터라고도 부름)이 
많아 공간적인 부분에서 낭비가 심함. 정제나 정규화 등으로 단어 집합의 크기를 
줄이는 것이 필요

2. 단순 빈도 수 기반 접근
정수 인코딩에서도 언급했었던 문제점으로 단어 간의 유사도를 표현할 수 없음.
불용어와 중요한 단어에 가중치를 부여하여 유사도를 표현하는 방법 -> TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency, 단어 빈도-역 문서 빈도)
DTM 내에 있는 각 단어에 대한 중요도를 계산할 수 있는 가중치를 주는 방법

d: 문서, t: 단어, n: 문서의 총 개수
tf(d, t): 특정 문서 d에서의 특정 단어 t의 등장 횟수 (Term-Frequency)
df(t): 특정 단어 t가 등장한 문서의 수 (documnent-frequency) 
idf(d, t): df(t)에 반비례하는 수 log(n/(1+df(t))) (inverse document frequency)
           log함수를 취하는 이유: 가중치가 기하급수적으로 증가하는 것을 막기 위하여
tf-idf = tf(d, t) * idf(d, t)
'''

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'you know I want your love',
    'I like you',
    'what should I do ',    
]

tfidfv = TfidfVectorizer().fit(corpus)          # 데이터 학습
print(tfidfv.fit_transform(corpus).toarray())   # 가중치를 부여하며 인코딩 및 DTM 생성
print(tfidfv.vocabulary_)