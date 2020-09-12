import pandas as pd

# df = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s1.txt')
# print(df)
# 그냥 불러오기.

# df = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s1.txt', skiprows=[0,1])
# print(df)
# 원하는 행을 삭제

# df = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s1.txt', skiprows=[0], header=None)
# print(df)
# 첫번째 행을 삭제한 후 새로운 header를 삽입 (None이므로 남은 행 중에서 첫번째 행이 자동으로 header가 되는 것을 막음. 따라서 기본적인 0 1 2 3 4 ~ 가 header로써 추가)

# df = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s1.txt', skiprows=[0], header=None, names=['Month',2013,2014,2015])
#print(df)
# names: 원하는 값을 header로써 추가

# df = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s1.txt', skiprows=[0], header=None, names=['Month',2013,2014,2015], index_col=[0])
# print(df)
# 특정 열을 index로써 지정

# df = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s1.txt', skiprows=[0], header=None, names=['Month',2013,2014,2015], index_col=[0], na_values=['JAN'])
# print(pd.isnull(df))
# print(df)
# 특정 값을 새로운 값으로 치환

# df = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s1.txt', skiprows=[0], header=None, names=['Month',2013,2014,2015])
# print(df)
# print(df.index)
# RangeIndex(start=0, stop=12, step=1)
# 0 ~ 12 개의 데이터가 있는 자료 1개

# print(list(df.index))
# print(df.index.values.tolist())
# 인덱스를 리스트화

# print(df.index.values)
# 인덱스의 값만 리스트화

# print(df.rename(index={0:'aa',1:'bb',2:'cc'}))
# 인덱스 값을 원하는 값으로 변경
# 일일이 하기 번거로움

# print(df.rename(index=lambda x:x+1))
# 인덱스를 0에서 +1씩 해서 새로 변경한다.

# df = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s2.txt', sep=';')
# print(df)
# j를 구분자로 선언하여 불러온다.

df2 = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s2.txt', sep=';', skiprows=[0], header=None, names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
# print(df)

# 평균 컬럼 추가
# df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
# print(df2)
# 특정 값을 바꾼다. 성적의 C를 A++ 교체

# df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1)
# print(df2)
# mean: 평균을 계산하는 함수
# axis=1 의 경우, 각 행의 평균 계산
# axis=0 의 경우, 각 열의 평균 계산

# df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
# print(df2)
# sum: 합계를 계산하는 함수
# axis=1 의 경우, 각 행의 합계 계산
# axis=0 의 경우, 각 열의 합계 계산