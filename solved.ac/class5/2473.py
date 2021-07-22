import sys; read = sys.stdin.readline

n = int(read())
t = list(map(int, read().split()))
acid = []; alkali = []
ans = int(1e10)
ret = []

for sol in t:
    if sol < 0:
        alkali.append(sol)
    else:
        acid.append(sol)

# 산성은 그냥 정렬, 알칼리성은 정렬 후 뒤집
acid.sort()
alkali.sort()
alkali = list(reversed(alkali))

# 산성 + 산성 + 알칼리
if len(acid) >= 2:
    ptr1 = 0; ptr2 = 1; ptr3 = 0    # 앞에 두 개는 산성 포인터, 나머지 하나는 알칼리 포인터
    while ptr2 < len(acid) and ptr3 < len(alkali):
        mix = acid[ptr1] + acid[ptr2] + alkali[ptr3]
        if mix == 0:
            print(alkali[ptr3], acid[ptr1], acid[ptr2])
            exit(0)
        if abs(mix) < abs(ans):
            ans = mix
            ret = [alkali[ptr3], acid[ptr1], acid[ptr2]]
        if mix > 0:
            ptr3 += 1
        else:
            # 다음 수와의 차이가 적은 쪽의 포인터를 먼저 당김
            if ptr1 + 1 == ptr2:
                ptr2 += 1
            elif ptr2 + 1 < len(acid):
                if acid[ptr1 + 1] - acid[ptr1] > acid[ptr2 + 1] - acid[ptr2]:
                    ptr2 += 1
                else:
                    ptr1 += 1
            else:
                ptr1 += 1

    if ptr2 == len(acid):
        for i in range(ptr1, ptr2-1):
            for j in range(ptr3, len(alkali)):
                mix = acid[i] + acid[ptr2-1] + alkali[j]
                if mix == 0:
                    print(alkali[j], acid[i], acid[ptr2-1])
                    exit(0)
                if abs(mix) < abs(ans):
                    ans = mix
                    ret = [alkali[j], acid[i], acid[ptr2-1]]
    
    if ptr3 == len(alkali):
        for i in range(ptr2, len(acid)):
            for j in range(ptr1, ptr2):
                mix = acid[j] + acid[i] + alkali[ptr3-1]
                if mix == 0:
                    print(alkali[ptr3-1], acid[j], acid[i])
                    exit(0)
                if abs(mix) < abs(ans):
                    ans = mix
                    ret = [alkali[ptr3-1], acid[j], acid[i]]


# 산성 + 알칼리 + 알칼리
if len(alkali) >= 2:
    ptr1 = 0; ptr2 = 1; ptr3 = 0
    while ptr2 < len(alkali) and ptr3 < len(acid):
        mix = alkali[ptr1] + alkali[ptr2] + acid[ptr3]
        if mix == 0:
            print(alkali[ptr2], alkali[ptr1], acid[ptr3])
            exit(0)
        if abs(mix) < abs(ans):
            ans = mix
            ret = [alkali[ptr2], alkali[ptr1], acid[ptr3]]
        if mix > 0:
            if ptr1 + 1 == ptr2:
                ptr2 += 1
            elif ptr2 + 1 < len(alkali):
                if alkali[ptr1] - alkali[ptr1+1] > alkali[ptr2] - alkali[ptr2+1]:
                    ptr2 += 1
                else:
                    ptr1 += 1
            else:
                ptr1 += 1
        else:
            ptr3 += 1

    if ptr2 == len(alkali):
        for i in range(ptr1, ptr2-1):
            for j in range(ptr3, len(acid)):
                mix = alkali[i] + alkali[ptr2-1] + acid[j]
                if mix == 0:
                    print(alkali[ptr2-1], alkali[i], acid[j])
                    exit(0)
                if abs(mix) < abs(ans):
                    ans = mix
                    ret = [alkali[ptr2-1], alkali[i], acid[j]]

    if ptr3 == len(acid):
        for i in range(ptr2, len(alkali)):
            for j in range(ptr1, ptr2):
                mix = alkali[i] + alkali[j] + acid[ptr3-1]
                if mix == 0:
                    print(alkali[i], alkali[j], acid[ptr3-1])
                    exit(0)
                if abs(mix) < abs(ans):
                    ans = mix
                    ret = [alkali[i], alkali[j], acid[ptr3-1]]

# 산성 * 3, 알칼리  * 3
if len(acid) >= 3:
    mix = acid[0] + acid[1] + acid[2]
    if abs(mix) < abs(ans):
        ans = mix
        ret = [acid[0], acid[1], acid[2]]

if len(alkali) >= 3:
    mix = alkali[0] + alkali[1] + alkali[2]
    if abs(mix) < abs(ans):
        ans = mix
        ret = [alkali[2], alkali[1], alkali[0]]

print(' '.join(str(x) for x in ret))