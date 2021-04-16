import numpy as np
import tensorflow as tf

x = np.array([[1,2],
              [3,4]])


# print(x.rank)   # 차원
print(x.shape)  # (2,2) => (1차원 행의 개수, 0차원 행의 개수)

# axis: 바깥 차원부터 0... 가장 안쪽 텐서의 axis = rank - 1
# print(tf.reduce_mean(x, axis=0))    # 열끼리 평균 냄
# print(tf.reduce_mean(x, axis=1))    # 행끼리 평균 냄

# 안쪽 텐서들을 합한 후 평균냄
print(tf.reduce_mean(tf.reduce_sum(x, axis=1)))

# argmax: 집계함수. 가장 큰 값의 인덱스 반환
print(tf.argmax(x, axis=0))

# reshape: 텐서의 shape를 바꿔줌
# one-hot: 텐서를 one-hot encoding 시켜버림. rank가 자동적으로 1만큼 expand됨
# zip: 복수 개의 텐서를 for문에 한꺼번에 넘길때 사용