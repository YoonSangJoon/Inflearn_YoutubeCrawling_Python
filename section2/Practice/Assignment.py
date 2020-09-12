import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="https://ssl.pstatic.net/tveta/libs/1285/1285288/243bc5b2fdb208a7bc26_20200519111013568.jpg"
mp4Url = "https://tvetamovie.pstatic.net/libs/1287/1287516/3adfda14a5d38d91a6dd_20200515161627840.mp4-pBASE-v0-f103113-20200515161854943.mp4"

savePath1 ="c:/Banner.jpg"
savePath2 = "c:/Movie.mp4"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(aviUrl).read()

saveFile1 = open(savePath1,'wb') # w : write , r : read , a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
