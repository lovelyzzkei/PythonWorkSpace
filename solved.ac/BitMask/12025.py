import sys; read = sys.stdin.readline
pw = read().strip()
k = int(read())
ans = {}; rest = {}
for i in range(len(pw)):
    if pw[i] in ('1', '2', '6', '7'):
        ans[i] = (int(pw[i]) + 5) % 5   # 가장 낮은 수로 만들기
    else:
        rest[i] = int(pw[i])

k = bin(k-1)[2:].zfill(len(ans))
if len(k) > len(ans):
    print(-1)
    exit(0)
else:
    key = list(ans.keys())
    for i in range(len(k)):
        if k[i] == '1':
            tmp = key[i]
            ans[tmp] = (ans[tmp]+5)%10
    ans.update(rest)
    ret = ''
    for i in range(len(pw)):
        ret += str(ans[i])
    # print(ans)
    # print(rest)
    print(ret)