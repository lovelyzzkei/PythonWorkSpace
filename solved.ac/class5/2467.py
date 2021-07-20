import sys; read = sys.stdin.readline

n = int(read())
acid = []; alkali = []; ans = int(1e10)
ret = []
t = list(map(int, read().split()))
for solution in t:
    if solution > 0: 
        acid.append(solution)
    else:   
        alkali.append(solution)
acid.sort()
alkali.sort()
alkali = list(reversed(alkali))
# print(acid)
# print(alkali)

ptr_acid = 0; ptr_alkali = 0
while ptr_acid < len(acid) and ptr_alkali < len(alkali):
    mix = acid[ptr_acid] + alkali[ptr_alkali]
    if abs(mix) < ans:
        ans = abs(mix)
        ret = [alkali[ptr_alkali], acid[ptr_acid]]
        if ans == 0:    # 정확하게 0이면 프로그램 종료
            break
    if mix < 0: # 혼합 용액의 특성값이 0보다 작으면 0에 가깝게 하기 위해 산성의 포인터를 증가
        ptr_acid += 1
    elif mix > 0:   # 반대로 0보다 크면 알칼리의 포인터를 증가
        ptr_alkali += 1

# 산성 용액끼리, 알칼리 용액끼리 혼합한 것이 더 작은지 확인
if len(acid) > 1:
    min_acid = acid[0] + acid[1]
    if abs(min_acid) < ans:
        ans = min_acid
        ret = [acid[0], acid[1]]

if len(alkali) > 1:
    min_alkali = alkali[0] + alkali[1]
    if abs(min_alkali) < ans:
        ans = min_alkali
        ret = [alkali[1], alkali[0]]
print(' '.join(str(x) for x in ret))