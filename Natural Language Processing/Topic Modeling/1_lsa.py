'''
잠재 의미 분석 (LSA) 구현
기존에 0이었던 값들은 0에 가까운 값들이 나오고 기존에 1이었던 값들은 1에 가까운 값들이 등장
=> 숨겨져 있던 의미들이 드러난다고 생각해도 무방
A = U'S'VT'
t: 토픽의 수
U': (m, t)의 크기 -> m개의 문서를 t개의 토픽로 표현 -> 각 행은 토픽을 표현하기 위한 문서 벡터들
S': (t, t)의 크기 -> 특이값 축소 -> 사용할 토픽을 t로 설정
VT': (t, n)의 크기 -> t개의 토픽은 n개의 단어로 표현 -> 각 행은 토픽을 표현하기 위한 단어 벡터들
'''

import numpy as np

# DTM 하나 생성. (4, 9) 크기
A = np.array([[0,0,0,1,0,1,1,0,0],[0,0,0,1,1,0,1,0,0],[0,1,1,0,2,0,0,0,0],[1,0,0,0,0,0,0,1,1]])

# 풀 SVD 수행
# U: (4, 4) 크기의 직교 행렬
# s: 특이값의 리스트가 반환됨 -> 대각 행렬로 변환 필요
# VT: (9, 9) 크기의 직교 행렬이 전치 행렬
U, s, VT = np.linalg.svd(A, full_matrices=True)

S = np.zeros((4, 9))
S[:4, :4] = np.diag(s)  # 특이값을 대각행렬에 삽입

# 특이값 분해가 잘 되었는지 확인, np.allclose()로 확인해도 무관
print(np.dot(np.dot(U, S), VT).round(2) == A)

# 풀 SVD로 U, S, VT를 구했으니 이를 가지고 절단된 SVD를 구하는 작업 수행, t=2
t = 2
U = U[:, :t]
S = S[:t, :t]
VT = VT[:t, :]

# print(U.round(2))
# print(S.round(2))
# print(VT.round(2))

# 절단된 SVD를 바탕으로 차원 축소된 A값 구하기
A_prime = np.dot(np.dot(U, S), VT)

# 기존 행렬 A와 비교
print(A)
print()
print(A_prime.round(2)) 