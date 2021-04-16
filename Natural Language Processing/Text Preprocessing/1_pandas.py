# Pandas: 파이썬 데이터 처리를 위한 라이브러리
import pandas as pd

'''
시리즈(Series)
데이터프레임(DataFrame)
패널(Panel)
'''

# 시리즈: 1차원 배열의 값(values)에 각 값에 대응되는 인덱스(index)를 부여할 수 있는 클래스
# sr = pd.Series([17000, 18000, 1000, 5000], index=["피자", "치킨", "콜라", "맥주"])
# print(sr)

'''
피자    17000
치킨    18000
콜라     1000
맥주     5000
dtype: int64
'''

# 데이터프레임: 2차원 리스트를 매개변수로 받음. 행방향 인덱스(index)와 열방향 인덱스(column), 그리고 교차하는 지점에 값(values)
# 총 3개의 값들로 구성되어 있음.

# values = [[1,2,3], [4,5,6], [7,8,9]]
# index = ['one', 'two', 'three']
# columns = ['A', 'B', 'C']

# df = pd.DataFrame(values, index=index, columns=columns)
# print(df)

'''
       A  B  C
one    1  2  3
two    4  5  6
three  7  8  9
'''

# 리스트, 딕셔너리로 데이터프레임 생성 가능
# 딕셔너리로 만들 경우 key값이 열 이름으로 설정됨
data = [
    ['1000', 'Steve', 90.72],
    ['1001', 'James', 78.09],
    ['1002', 'Doyeon', 98.43],
    ['1003', 'Jane', 64.19],
    ['1004', 'Filwoong', 81.30],
    ['1005', 'Tony', 99.14],
]

df = pd.DataFrame(data, columns=['학번', '이름', '점수'])   # 행, 열 설정 가능
print(df.head(3))   # head(n): 앞의 n개의 데이터 참조
print(df.tail(3))   # tail(n): 뒤의 n개의 데이터 참조
print(df['점수'])   # 열 이름으로 열 참조 가능

# csv, txt, xlsx 등의 파일들을 읽어올 수 있음
'''
df = pd.read_csv(...)
'''
