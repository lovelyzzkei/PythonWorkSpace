import pandas as pd

# 두 시트를 상품ID 칼럼에 대해 합침
df1 = pd.read_excel('판매 데이터.xlsx', '판매 이력')
df2 = pd.read_excel('판매 데이터.xlsx', '상품정보')

df3 = pd.merge(df1, df2, on='상품ID')

print(df3)

# 트랜잭션 테이블을 피벗 테이블로 변환
df4 = pd.pivot_table(df3,                          # 피벗 테이블로 전환할 data frame 
                    index=['상품명', '점포ID'],     # 행 위치에 들어갈 항목
                    columns='매출일',               # 열 위치에 들어갈 항목
                    values='금액')                  # 행과 열이 교차하는 지점에 들어갈 데이터

print(df4)

# 스크립트에서 동적으로 칼럼 생성
def category(row):
    return {101:'식료품'}.get(row['상품ID'], '그 외')

df1['상품 카테고리'] = df1.apply(category, axis=1)
print(df1)
