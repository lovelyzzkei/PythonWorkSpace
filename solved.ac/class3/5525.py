import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

# Pn 생성
Pn = ''
for i in range(1, 2*(N+1)):
    if i % 2 == 1:
        Pn += 'I'
    else:
        Pn += 'O'

cnt = 0

# 라빈-카프 알고리즘 사용
def findString(parent, pattern):
    global cnt

    parentSize = len(parent)
    patternSize = len(pattern)
    parentHash = 0; patternHash = 0; power = 1

    for i in range(parentSize - patternSize + 1):
        if i == 0:
            for j in range(patternSize):
                parentHash += ord(parent[patternSize - 1-  j]) * power
                patternHash += ord(pattern[patternSize - 1 - j]) * power
                if (j < patternSize - 1):
                    power *= 2
        
        else:
            parentHash = 2 * (parentHash - ord(parent[i-1]) * power) + ord(parent[patternSize - 1 + i])

        if parentHash == patternHash:
            finded = True
            for j in range(patternSize):
                if parent[i+j] != pattern[j]:
                    finded = False
                    break

            if finded:
                cnt += 1

findString(S, Pn)
print(cnt)