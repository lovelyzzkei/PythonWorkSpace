'''
PADDING
각 문장의 길이는 다름. 컴퓨터는 같은 길이의 문장에 대해서는 묶어서 처리가 가능
=> 병렬 연산을 통한 처리 속도 개선을 위해서는 임의로 길이를 통일시키는 작업이 필요
=> 이때 사용하는 것이 Padding
'''

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], 
['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], 
['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], 
['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], 
['barber', 'went', 'huge', 'mountain']]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)                   # 정수 인코딩
encoded = tokenizer.texts_to_sequences(sentences)   # sentences에 맵핑

# 길이를 통일시키기 위해 가장 길이가 긴 문장의 길이 계산
max_len = max(len(item) for item in encoded)    # 7

# 각 sentence에 0을 추가하여 길이를 모두 7로 맞춤 => 제로 패딩(zero padding)
# 0은 의미가 없기 때문에 컴퓨터는 이를 무시할 것
for s in encoded:
    while len(s) < max_len:
        s.append(0)

padded_np = np.array(encoded)

###########################################################################
# keras에 패딩 도구 존재
from tensorflow.keras.preprocessing.sequence import pad_sequences

encoded = tokenizer.texts_to_sequences(sentences)

# 기본적으로 문장의 앞에 패딩, 뒤에 채우려면 padding='post'를 주면 됨, 넘파이 배열 반환
# maxlen parameter를 가지고 문장 길이 조절 가능
# value parameter를 가지고 padding하는 값 조절 가능
padded = pad_sequences(encoded, padding='post')     

print(padded)