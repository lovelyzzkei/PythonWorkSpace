import sys
from collections import deque

T = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for testcase in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())

    # 문서 받기
    doc = list(map(int, sys.stdin.readline().strip().split()))
    target = doc[M]
    
    # 만약 문서의 중요도가 모두 다르다면 중요도가 큰 것부터 차례대로 빠진다
    if len(set(doc)) == len(doc):
        print(sorted(doc, reverse=True).index(target) + 1)

    else:
        # 중요도가 중복되는 문서가 존재할 경우
        new_doc = []

        # 우리가 찾고 있는 문서라는 것을 확인하기 위한 boolean을 같이 넣어줌
        for i in range(N):
            if i != M:
                new_doc.append([doc[i], False])
            else:
                new_doc.append([doc[i], True])
        doc = deque(new_doc)
        # 순서를 확인하기 위한 변수 설정
        cnt = 0
        while True:
            
            if doc[0][0] == max(t[0] for t in list(doc)):
                cnt += 1
                if doc[0][1]:
                    break
                else:
                    doc.popleft()
                
            else:
                doc.append(doc.popleft())
                

        print(cnt)
