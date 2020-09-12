import pandas as pd

df = pd.read_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1.xlsx', header=0)
# print(df)

# 컬럼 값 수정
# print(df['State']) # State 값만 불러오기
df['State'] = df['State'].str.replace('','|') # State 값 사이사이에 | 추가
# print(df)

# 평균 컬럼 추가
df['Avg'] = df[['2003','2004','2005']].mean(axis=1).round(2)
# 각 행의 값의 평균을 나타내는 Avg 열 새로 추가
# round(2): 소숫점 2째 자리까지 나타낸다.
# print(df)

# 합계 컬럼 추가
df['Sum'] = df[['2003','2004','2005']].sum(axis=1).round(2)
# print(df)

# 최대값 출력
# print(df[['2003','2004','2005']].max(axis=0))

# 최소값 출력
# print(df[['2003','2004','2005']].min(axis=0))

# 상세 정보 출력
# print(df.describe())
# 여러 계산 정보를 요약해서 표시

# df.to_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1_modification.xlsx', index=None)
# index=None: 인덱스 없애기
# print(df)