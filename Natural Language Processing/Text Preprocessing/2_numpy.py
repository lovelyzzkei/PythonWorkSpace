# numpy: 다차원 행렬 자료구조인 ndarray. 벡터 및 선형 대수 계산. 빠른 속도
import numpy as np
from numpy.core.fromnumeric import reshape

# 1차원 array
# a = np.array([1,2,3,4,5])
# print(type(a))      # <class 'numpy.ndarray'>
# print(a)            # [1 2 3 4 5]

# 2차원 array
# b = np.array([[1,2,3], [4,5,6]])
# print(b)
# print(b.ndim)       # 2
# print(b.shape)      # (2, 3)

# a = np.zeros((2, 3))    # zeros(a, b): shape를 (a, b)로 하며 모든 값을 0로 초기화
# a = np.ones((2, 3))     # ones(a, b): shape를 (a, b)로 하며 모든 값을 1로 초기화 
# a = np.full((2, 2), 7)  # full(): shape가 (2, 2)이며 모든 값을 특정 상수로 초기화, 여기서는 7
# a = np.eye(3)           # eye(n): shape가 (n, n)인 대각 행렬 생성
# print(a)

# np.arrange(start, stop, step, dtype): 지정 범위에 대하여 배열을 생성
# start 부터 stop-1까지 step만큼 증가하는 배열
# a = np.arrange(1, 10, 2)    # [1,3,5,7,9]

# reshape(): 배열을 다차원으로 변형
# a = np.array(np.arange(30)).reshape((5, 6))
# print(a)

# numpy slicing
# 각 차원별로 slicing을 해주어야 한다.
a = np.array([[1,2,3], [4,5,6]])
# print(a[0:2, 0:2])      # [[1,2], [4,5]]
print(a[:, 0])            # 첫번째 열 출력: [1,4]
print(a[0, :])            # 첫번째 행 출력: [1,2,3]
