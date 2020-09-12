import pandas as pd

df2 = pd.read_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s2.txt', sep=';', skiprows=[0], header=None, names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
# print(df)

# 평균 컬럼 추가
# df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
# print(df2)

# df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1)
# print(df2)

# df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
# print(df2)


df2.to_csv('C:\\Pythonsource\\Workspace\\Crawling\\section4\txt\\result_s1.txt', index=False)
# index=False: 인덱스를 없앤다.