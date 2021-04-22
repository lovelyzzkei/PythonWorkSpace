'''
LDA 실습
'''

import re
import gensim
import pyLDAvis
import pyLDAvis.gensim_models
import pandas as pd 
from nltk.corpus import stopwords
from sklearn.datasets import fetch_20newsgroups
from gensim import corpora

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
print(tokenized_doc[1])

# LSA에서와 동일한 데이터 사용
# 정수 인코딩과 단어의 빈도수 기록을 동시에 진행
dictionary = corpora.Dictionary(tokenized_doc)
corpus = [dictionary.doc2bow(text) for text in tokenized_doc] # (word_idx, word_freq) 형태로 구성되어있음

# 토픽의 개수를 20으로 하여 학습

NUM_TOPICS = 20

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)


# LDA 시각화. 각 토픽들의 단어들의 분포 확인
vis = pyLDAvis.gensim_models.prepare(ldamodel, corpus, dictionary)
pyLDAvis.enable_notebook()
pyLDAvis.display(vis)

# 문서별 토픽 문포 확인
# ldamodel에 전체 데이터가 정수 인코딩 된 결과를 넣으면 확인 가능
for i, topic_list in enumerate(ldamodel[corpus]):
    if i == 5:
        break
    print(i, "번째 문서의 topic 비율은", topic_list)
