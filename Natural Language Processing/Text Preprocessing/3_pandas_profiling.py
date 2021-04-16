"""
데이터의 성격을 파악하는 과정
데이터 내 값의 분포, 변수 간의 관계, 결측값(missing values)의 유무 등을 파악하는 과정
=> EDA(Exploratory Data Analysis, 탐색적 데이터 분석)
이를 실행해주는 pandas profiling
"""

import pandas as pd
import pandas_profiling 

# 데이터 불러오기
data = pd.read_csv('spam.csv', encoding='latin1')

pr = data.profile_report()
