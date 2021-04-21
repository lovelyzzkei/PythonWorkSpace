'''
LSA 실습
: 20개의 다른 주제를 가진 뉴스그룹 데이터를 가지고 문서의 수를 원하는 토픽의 수로 압축한 뒤
각 토픽당 가장 중요한 단어 5개를 출력하는 실습
'''

import pandas as pd 
from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
documents = dataset.data    # 11314개

print(documents[1])
# 텍스트 전처리
# 구두점, 숫자, 특수문자, 길이가 짧은 단어 제거
news_df = pd.DataFrame({'documents':documents})