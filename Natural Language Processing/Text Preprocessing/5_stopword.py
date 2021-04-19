import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('punkt')
# nltk.download('stopwords')

example = "Family is not an important thing. It's everything."

stop_words = list(set(stopwords.words('english')))
print(stop_words[:5])   # ['some', 'own', "mustn't", 'me', 'over']

# 문장을 단어 토큰화
word_token = word_tokenize(example)

# 불용어 제거
result = []
for w in word_token:
    if w not in stop_words:
        result.append(w)

print(word_token)
print(result)