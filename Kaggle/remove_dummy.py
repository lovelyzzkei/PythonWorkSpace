import shutil
import glob
import pandas as pd

def strSlice(name):
    return name[:-4]

def fileLoc(dirName):
    locList = glob.glob("D:/deepfake_1st/fake/*/*/*/fsgan/" + dirName)
    return locList

# csv 파일 불러와 파일들 이름과 위치의 리스트 생성
src = pd.read_csv('서울대_변조_의심_영상.csv')
name = src['name'].tolist()
location = src['location'].tolist()


# 뒤에 .mp4 제거
name = list(map(strSlice, name))
# print(name)


# 변조 영상 폴더들 모두 삭제
for video in name:
    locList = fileLoc(video)
    print(locList)
    shutil.rmtree(locList[0])

