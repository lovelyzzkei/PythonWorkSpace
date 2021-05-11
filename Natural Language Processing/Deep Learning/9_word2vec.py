import urllib.request
import zipfile
import re
from lxml import etree
from nltk.tokenize import word_tokenize, sent_tokenize
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

# 데이터 다운로드
urllib.request.urlretrieve("https://raw.githubusercontent.com/GaoleMeng/RNN-and-FFNN-textClassification/master/ted_en-20160408.xml", filename="ted_en-20160408.xml")

# 훈련 데이터가 XML 문법으로 작성되어 있어 자연어를 얻기 위해서는 전처리가 필요
# 필요한 데이터는 <content> 태그 내의 내용들
# 여기에 <content> 태그 내의 내용들 중 필요없는 내용들을 추가적으로 제거해주어야 함.

# 데이터 전처리
targetXML = open('ted_en-20160408.xml', 'r', encoding='UTF8')
target_text = etree.parse(targetXML)

# xml 파일로부터 <content> 태그 사이의 내용만 가져옴
parse_text = '\n'.join(target_text.xpath('//content/text()'))

# 정규 표현식의 sub 모듈을 이용하여 content 중간에 나오는 괄호 내용들 모두 제거
content_text = re.sub(r'\([^)]*\)', '', parse_text)

# NLTK를 이용하여 문장 토큰화
sent_text = sent_tokenize(content_text)

# 각 문장에 대해 구두점 제거, 소문자화
normalized_text = []
for string in sent_text:
    tokens = re.sub(r"[^a-z0-9]+", " ", string.lower())
    normalized_text.append(tokens)

# 각 문장에 대해 NLTK를 이용하여 단어 토큰화
result = [word_tokenize(sentence) for sentence in normalized_text]

# Word2Vec 모델에 텍스트 데이터 훈련 
model = Word2Vec(sentences=result, 
                 vector_size=100,          # 임베딩 벡터의 차원
                 window=5,          # 윈도우 크기
                 min_count=5,       # 단어 최소 빈도 수 제한
                 workers=4,         # 학습을 위한 프로세스 수
                 sg=0)              # 0이면 CBOW, 1이면 Skip-Gram

# 모델에 man과 유사한 단어 출력 지시
model_result = model.wv.most_similar("man")
print(model_result)

model.wv.save_word2vec_format('eng_w2v')