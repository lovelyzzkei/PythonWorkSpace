'''
INTEGER ENCODING
텍스트를 숫자로 바꾸기 위한 여러가지 기법들.
WHY? 컴퓨터는 텍스트보다는 숫자를 더 잘 처리하기 때문
보통 전처리 또는 빈도수가 높은 단어들만 사용하기 위하여 단어의 빈도수를 기준으로 정렬 후 인덱스 부여
'''

# dictionary 사용하기
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "A barber is a person. a barber is good person. \
    a barber is huge person. he Knew A Secret! \
    The Secret He Kept is huge secret. Huge secret. His barber kept his word. \
    a barber kept his word. His barber kept his secret. \
    But keeping and keeping such a huge secret to himself was driving the barber crazy.\
    the barber went up a huge mountain." 

# 문장 토큰화
text = sent_tokenize(text)

# 정제 작업을 하며 단어 토큰화 수행
vocab = {}
sentences = []
stopwords = set(stopwords.words('english'))

for i in text:
    sentence = word_tokenize(i)     # 각 문장에 대해 단어 토큰화
    result = []

    for word in sentence:           # 정제 작업
        word = word.lower()         # 대, 소문자 통합
        if word not in stopwords:   # 불용어 제거
            if len(word) > 2:       # 짧은 단어 제거 ex) a, the, ...
                result.append(word)
                if word not in vocab:   # 단어의 빈도수 체크
                    vocab[word] = 0
                vocab[word] += 1

    sentences.append(result)

# 빈도수가 높은 순으로 정렬
# key=lambda x:x[1] => 정렬하는 item 중에서 두번째 값을 기준으로 정렬, reverse=True => 내림차순
vocab_sorted = sorted(vocab.items(), key=lambda x:x[1], reverse=True)
# print(vocab_sorted)

word_to_index = {}
i = 0

for (word, frequency) in vocab_sorted:
    if frequency > 1:       # 빈도수가 적은 단어는 제외
        i += 1
        word_to_index[word] = i

# 빈도수가 가장 높은 5개의 단어만 사용
vocab_size = 5
words_frequency = [w for w,c in word_to_index.items() if c >= vocab_size + 1]   # 인덱스가 5를 초과하는 단어 삭제

for w in words_frequency:
    del word_to_index[w]    # 해당 단어의 인덱스 정보 삭제


# INTEGER ENCODING 진행, sentences의 단어들을 정수로 맵핑
# 이때 dictionary에 없는 단어(OOV, Out-Of-Vocabulary)들은 'OOV'로 처리
word_to_index['OOV'] = len(word_to_index) + 1

encoded = []
for s in sentences:
    temp = []
    for w in s:
        try:
            temp.append(word_to_index[w])
        except:     # 예외 처리
            temp.append(word_to_index['OOV'])
    encoded.append(temp)

#####################################################################

# 좀 더 쉬운 방법: Counter
from collections import Counter

# 단어 집합을 만들기 위해 sentences에서 문장의 경계인 ,를 제거하고 단어들을 하나의 리스트로 만듦
words = sum(sentences, [])
vocab = Counter(words)  # 위에서 한 빈도수 체크와 동일한 결과. Counter Object반환. 딕셔너리 형태

vocab = vocab.most_common(vocab_size)   # 빈도수가 높은 단어들을 vocab_size만큼 반환
# print(vocab)

#####################################################################

# NLTK에서는 빈도수 계산도구인 FreqDist() 사용
from nltk import FreqDist
import numpy as np

vocab = FreqDist(np.hstack(sentences))    # hstack(): 배열을 가로로 결합 -> 쉼표 모두 제거됨
vocab = vocab.most_common(vocab_size)
# print(vocab)

word_to_index = {word[0] : index + 1 for index, word in enumerate(vocab)}   # enumerate를 이용하여 인덱스 부여를 간단하게
# print(word_to_index)

#####################################################################

# Keras에서 INTEGER ENCODING
from tensorflow.keras.preprocessing.text import Tokenizer

# num_words: 인코딩에 사용할 단어의 개수. 숫자를 0부터 카운팅하기 때문에 1을 더해줌, oov_token: OOV에 대하여 설정해줌, 기본적인 인덱스는 1
tokenizer = Tokenizer(num_words=vocab_size+2, oov_token='OOV')

# fit_on_texts(): 입력한 텍스트로부터 단어 빈도수가 높은 순으로 낮은 정수 인덱스를 부여. 앞에서의 작업과 동일
tokenizer.fit_on_texts(sentences)  
# print(tokenizer.word_index) 

# text_to_sequences(): 입력으로 들어온 코퍼스에 대해 각 단어를 정해져있는 인덱스로 변환. 인코딩 작업
print(tokenizer.texts_to_sequences(sentences))  
print(sentences)