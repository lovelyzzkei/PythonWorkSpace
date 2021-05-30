import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().strip().split()))

cards_counts = {}
cards.sort()
idx = cards[0]
cards_counts[idx] = 1
for i in range(1, len(cards)):
    if idx != cards[i]:
        cards_counts[cards[i]] = 1
        idx = cards[i]
    else:
        cards_counts[idx] += 1

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().strip().split()))
cnt = []

for target in targets:
    try:
        cnt.append(cards_counts[target])
    except:
        cnt.append(0)

for num in cnt:
    print(num, end=" ")