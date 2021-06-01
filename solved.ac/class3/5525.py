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

pi = [0 for i in range(len(Pn))]
ret = []

# KMP 알고리즘 사용
def getPartialMatch(pattern):
    m = len(pattern)

    # KMP로 자기 자신 찾기
    # begin=0이면 자기 자신을 찾는 것이니까 패스
    begin = 1; matched = 0

    # 비교할 문자가 pattern의 끝에 도달할 때까지 찾으면서 부분 일치를 모두 기록
    while begin + matched < m:
        if pattern[begin + matched] == pattern[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]

def KMP(parent, pattern):
    n = len(parent)
    m = len(pattern)
    getPartialMatch(pattern)

    begin = 0; matched = 0

    while begin <= n - m:
        if matched < m and parent[begin+matched] == pattern[matched]:
            matched += 1
            if matched == m:    ret.append(begin)
        
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    
KMP(S, Pn)
print(len(ret))