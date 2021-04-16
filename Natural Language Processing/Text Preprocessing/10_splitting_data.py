'''
SPLITTING DATA (데이터의 분리)
머신 러닝 모델에 데이터를 훈련시키기 위해서는 데이터를 적절히 분리하는 작업이 필요.
지도 학습(Supervised Learning)을 위한 데이터 분리 작업
데이터를 먼저 문제와 정답으로 분리  => 이 데이터들 중 일부를 테스트 데이터로 분리

<훈련 데이터>   => 모델이 학습하는 데이터
x_train: 문제지 데이터
y_train: 문제지에 대한 정답 데이터

<테스트 데이터> => 모델이 맞춰야하는 데이터. x_test에 대한 정답을 예측. 예측하여 맞은 점수가 정확도
x_test: 시험지 데이터
y_test: 시험지에 대한 정답 데이터

'''

# zip 함수를 이용하여 분리
# '*'를 사용하여 첫번째 원소, 두번째 원소들끼리 다시 압축
sequences = [['a', 1], ['b', 2], ['c', 3]]
x, y = zip(*sequences)    # ('a', 'b', 'c') (1, 2, 3)

# 데이터프레임을 이용하여 분리
import pandas as pd

values = [['당신에게 드리는 마지막 혜택!', 1],
['내일 뵐 수 있을지 확인 부탁드...', 0],
['도연씨. 잘 지내시죠? 오랜만입...', 0],
['(광고) AI로 주가를 예측할 수 있다!', 1]]
columns = ['메일 본문', '스팸 메일 유무']

df = pd.DataFrame(values, columns=columns)
x = df[columns[0]]
y = df[columns[1]]

#####################################################################
# 테스트 데이터 분리
# 이미 분리가 되어있는 x, y 데이터에서 테스트 데이터를 분리하는 과정

# 사이킷 런을 이용
from sklearn.model_selection import train_test_split

# test_size: x, y 데이터에서 0.2만큼 test로 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)
print(x_train, x_test)