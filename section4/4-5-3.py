import pandas as pd
import numpy as np
# 파이썬에서 데이터분석을 하기 위해 필요한 pandas와 numpy
# 수치 데이터를 계산할 때 numpy가 유용

# 랜덤으로 DataFrame 생성
# df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=list('ABCD'))
# print(df)

# df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=['A', 'B', 'C', 'D'])
# print(df)

df = pd.DataFrame(np.random.randn(100,4), columns=['A', 'B', 'C', 'D'])
print(df)

df.to_csv('C:\Pythonsource\Workspace\Crawling\section4\txt\csv_s2.txt', index=False, header=False)
# header=False: 헤더를 없앰