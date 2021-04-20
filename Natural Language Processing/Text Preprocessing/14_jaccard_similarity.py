'''
자카드 유사도
두 문서에 등장하는 모든 단어들 중 두 문서에 공통적으로 등장하는 단어들의 비율
합집합에서 교집합의 비율
'''

doc1 = "apple banana everyone like likey watch card holder"
doc2 = "apple banana coupon passport love you"

tokenized_doc1 = set(doc1.split())
tokenized_doc2 = set(doc2.split())

# 교집합, 합집합, 차집합 -> set 자료형 이용
# union(): set 자료형의 합집합
union = tokenized_doc1 | tokenized_doc2
intersection = tokenized_doc1 & tokenized_doc2

jaccard_sim = len(intersection) / len(union)
print(jaccard_sim)