'''
머신러닝 워크 플로우
데이터 수집 -> 점검 및 탐색 -> 전처리 및 정제 -> 모델링 및 훈련 -> 평가 -> 배포
점검 및 탐색은 앞에서 배운 pandas_profiling을 통하여 탐색
이를 통해 얻은 정보를 바탕으로 전처리 및 정제
'''
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
text = "Don't be fooled by the dark sounding name, Mr.Jone's Orphanage is as cheery as cheery goes for a pastry shop."
print(tokenizer.tokenize(text))