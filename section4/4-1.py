import pickle
# (객체, 텍스트) 직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = "C:\\Pythonsource\\Workspace\\Crawling\\section4\\Test\\test.bin"
tfilename = "C:\\Pythonsource\\Workspace\\Crawling\section4\\\Test\\test.txt"

data1 = 77
data2 = 'hello, world!'
data3 = ['car','apple','house']

# 바이너리 쓰기
with open(bfilename, 'wb') as f:
    # wb : write binary
    pickle.dump(data1,f)
    pickle.dump(data2,f)
    pickle.dump(data3,f)
# dump: 객체를 바이너리에 쓸 때 사용.
# dumps: 문자열을 직렬화할 때 사용.

# 텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))
    # 리스트 형식의 데이터를 쓸 때 사용.

# 바이너리 읽기
with open(bfilename, 'rb') as f:
    # rb : read binary
    b = pickle.load(f) # loads (문자열 역직렬화)
    print(type(b), ' Binary Read1 \ ', b)
    b = pickle.load(f)
    print(type(b), ' Binary Read2 \ ', b)
    b = pickle.load(f)
    print(type(b), 'Binary Read3 \ ', b)
# pickle을 이용한 바이너리는 해당 자료형을 그대로 복원

# 텍스트 읽기
with open(tfilename, 'rt') as f:
    # rt : read textline
    for i, line in enumerate(f,1):
        print(type(line),'Text Read' + str(i) + ' \ ',line,end='')

# 텍스트파일로 작성한 자료는 다시 불러와도 str 형식으로 변환
# 2차 가공이 필요