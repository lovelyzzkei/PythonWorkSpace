# sklearn을 이용하여 LDA 수행
# 뉴스 기사 제목 데이터에 대한 이해

import nltk
import pandas as pd
import urllib.request
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


# 뉴스 기사 제목 데이터 준비
urllib.request.urlretrieve("https://raw.githubusercontent.com/franciscadias/data/master/abcnews-date-text.csv", filename="abcnews-date-text.csv")
data = pd.read_csv('abcnews-date-text.csv', error_bad_lines=False)  # 100만개의 샘플

# 제목 부분만 필요하므로 따로 저장
text = data[['headline_text']]

# 텍스트 전처리
# 불용어 제거, 표제어 추출, 길이가 짧은 단어 제거
# NLTK의 word_tokenize로 토큰화 진행
text['headline_text'] = text.apply(lambda row: nltk.word_tokenize(row['headline_text']), axis=1)

# 불용어 제거
nltk.download('wordnet')

stop = stopwords.words('english')
text['headline_text'] = text['headline_text'].apply(lambda x: [w for w in x if w not in stop])

# 표제어 추출
# 3인칭 단수 표현 -> 1인칭, 과거 현재형 동사 -> 현재형
text['headline_text'] = text['headline_text'].apply(lambda x: [WordNetLemmatizer().lemmatize(word, pos='v') for word in x])

# 길이가 짧은 단어 제거
tokenized_doc = text['headline_text'].apply(lambda x: [w for w in x if len(w) > 3])


# 전처리 끝
# TF-IDF 행렬 생성
# 먼저 역 토큰화
detokenized_doc = []
for i in range(len(text)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

text['headline_text'] = detokenized_doc

# 이후 TF-IDF 행렬 생성
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(text['headline_text'])

# 토픽 모델링
from sklearn.decomposition import LatentDirichletAllocation

lda_model = LatentDirichletAllocation(n_components=10, learning_method='online',
                    random_state = 777, max_iter=1)

terms = vectorizer.get_feature_names() # 단어 집합. 1,000개의 단어가 저장됨.

def get_topics(components, feature_names, n=5):
    for idx, topic in enumerate(components):
        print("Topic %d:" % (idx+1), [(feature_names[i], topic[i].round(2)) for i in topic.argsort()[:-n - 1:-1]])

print(get_topics(lda_model.components_,terms))