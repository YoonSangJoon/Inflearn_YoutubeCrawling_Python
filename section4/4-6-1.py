import pandas as pd
# xlrd, openpyxl

# 기본 읽기 1
# df = pd.read_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1.xlsx')
# print(df)

# 엑셀의 특정 sheet 불러오기 (0 1 2 ~)
# df = pd.read_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1.xlsx', sheet_name=0)
# print(df)
# print(df.head()) # 상위 5개 부문만 표시
# print(df.tail()) # 하위 5개 부문만 표시

# 특정 행 생략
# df = pd.read_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1.xlsx', skiprows=[0], skip_footer=10)
# print(df)
# skip_footer: 하위 10개 행을 제외하고 불러오기

# 특정 행을 header로 선언 (기본 0)
# df = pd.read_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1.xlsx', header=1)
# print(df)
# print(list(df)) # header부분만 리스트화
# print(list(df.columns.values)) # 똑같음

# header 새로 정의
# df = pd.read_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1.xlsx', skiprows=[0], header=None, names=['State',2003,2004,2005])
# print(df)

# 특정 값 치환
# df = pd.read_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1.xlsx', header=0, na_values='...', converters={'2003': lambda w: w if w > 60000 else None})
# # print(df)
# # converters: 2003 열에서 60000 이상인 값만 표시
# print(pd.isnull(df)) # null인 값만 True

# 실습 정리 및 인덱스 재정의
# df = pd.read_excel('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xlsx\\excel_s1.xlsx', header=0)
# print(df.rename(index=lambda x:x+1))
# print(df.rename(index=lambda x:x+1).index) # index만 출력
