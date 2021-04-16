import re

# .: .자리에 임의의 문자 1개
# r = re.compile("ab.")   # ab.: abc, abd, abe, ...
# r1 = r.search("kkkabc")  # search(): 문자열 전체에서 정규 표현식에 해당하는 부분을 search => abc, Match Object 반환
# r2 = r.match("kkkabc")   # match(): 문자열 첫 부분부터 매치 => 아무것도 출력되지 않음


# findall(): 정규 표현식과 매치되는 모든 문자열들을 리스트로 리턴, 없으면 빈 리스트 리턴
# \d: 모든 숫자, +: 문자가 1개 이상
# text="""
# Regular expression : A regular expression, regex or regexp[1]
# """  

# re.findall("\d+", text)     # ['010', '1234', '1234', '30']

# sub(): 정규 표현식 패턴과 일치하는 문자열을 찾아 다른 문자열로 대체
# [^a-zA-Z\s]: 공백과 문자를 제외한 문자열
# print(re.sub('[^a-zA-Z\s]', ' ', text))

# 정규 표현식 텍스트 전처리 예제
text = """100 John    PROF
101 James   STUD
102 Mac   STUD""" 

# 텍스트의 공백 없애기
re.split("\s+", text)

# 텍스트에서 숫자만 뽑아내기
re.findall('\d+', text)

# 텍스트에서 대문자인 행의 값만 가져오기
r = re.findall('[A-Z]{4}', text)

# 텍스트에서 이름만 가져오기
r = re.findall('[A-Z][a-z]+', text)
print(r)

# 정규표현식을 이용한 토큰화
import nltk
from nltk.tokenize import RegexpTokenizer

# 문장에서 문자열들만 뽑아내기. 특수문자, 구두점 모두 제외
tokenizer = RegexpTokenizer('[\w]+')
print(tokenizer.tokenize("Don't be fooled by the dark sounding name, \
    Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop"))