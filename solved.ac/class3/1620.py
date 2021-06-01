import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_encyclopedia = [0]
pokemon_name = {}

# 포켓몬 도감에 저장
for i in range(1, N+1):
    pokemon = sys.stdin.readline().strip()
    pokemon_encyclopedia.append(pokemon)
    pokemon_name[pokemon] = i

for _ in range(M):
    test = sys.stdin.readline().strip()

    try:    # 문제가 포켓몬 번호일 경우
        test = int(test)
        print(pokemon_encyclopedia[test])
    except: # 문제가 포켓몬 이름일 경우
        print(pokemon_name[test])