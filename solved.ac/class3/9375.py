import sys; read=sys.stdin.readline

ret = []
for t in range(int(read())):
    dress = {}
    # 가지고 있는 옷들 저장
    for n in range(int(read())):
        name, kind = read().strip().split()
        try:
            dress[kind] += 1
        except:
            dress[kind] = 1
    
    ans = 1
    values = dress.values()

    # 전체 조합의 가짓수는 (a+1)(b+1)(c+1)...(n+1)-1
    for value in values:
        ans *= (value + 1)

    ret.append(ans-1)
      

print('\n'.join(str(x) for x in ret))