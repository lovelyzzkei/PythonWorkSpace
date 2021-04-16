import pandas as pd

# 두 시트 받아오기
df1 = pd.read_excel(u'판매 데이터.xlsx', u'시트1')
df2 = pd.read_excel(u'판매 데이터.xlsx', u'상품정보')

# 두 시트를 상품ID에 대하여 합침
df3 = pd.merge(df1, df2, on='상품ID')

# 합친 시트를 피벗 테이블로 변환
# values: 데이터로 사용할 열
# index: 행 위치에 들어갈 열
# columns: 열 위치에 들어갈 열
# aggfunc: 데이터 집계 함수
print(df3.pivot_table(values=u'금액', index=[u'점포ID', u'상품명'], columns=u'매출일', aggfunc='sum'))

# 함수로 상품 카테고리 생성
def category(row):
    return {101:u'식료품'}.get(row[u'상품ID'], u'그 외')

# 카테고리 적용
df1[u'상품 카테고리'] = df1.apply(category, axis=1)
print(df1)