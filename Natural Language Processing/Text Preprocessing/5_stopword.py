import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english'))
print(stop_words)

word_token = word_tokenize(example)

result = []
for w in word_token:
    if w not in stop_words:
        result.append(w)

print(word_token)
print(result)