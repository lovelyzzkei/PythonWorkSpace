'''
라빈-카프 알고리즘
: 문자열을 검색하는 알고리즘 중 하나
  찾는 문자열의 해시값을 구한 뒤 원 문자열에서 찾는 문자열의 길이만큼을 해싱하면서
  해시값이 일치하면 두 문자열을 비교하여 일치하는지를 확인하는 알고리즘
  준수한 속도를 보이지만 원 문자열의 길이가 너무 길 경우 해시값이 불어날 수 있으므로
  좀 더 안정적인 성능의 알고리즘을 만드려면 모듈러 연산을 추가해주는 것이 좋다  
  
  해시값 = sum(2 ** power * ord(해당 문자))
'''
INF = 1234567891

def RabinCarf(parent, pattern):
    parentSize = len(parent)
    patternSize = len(pattern)
    parentHash = 0; patternHash = 0; power = 1  # 

    for i in range(parentSize - patternSize + 1):
        # 찾는 문자열과 원 문자열 모두 해싱
        if i == 0:  
            for j in range(patternSize):
                parentHash += (ord(parent[patternSize - 1 - j]) * power) % INF
                patternHash += (ord(parent[patternSize - 1 -j]) * power) % INF
                if j < patternSize - 1:
                    power *= 2


        else:
            parentHash = (2 * (parentHash - ord(parent[i-1]) * power) + ord(parent[patternSize - 1 + i])) % INF

        if parentHash == patternHash:
            finded = True
            for j in range(patternSize):
                if parent[i+j] != pattern[j]:
                    finded = False
                    break

            if finded:
                cnt += 1