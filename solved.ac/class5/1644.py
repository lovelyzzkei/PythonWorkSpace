import sys; read = sys.stdin.readline
import heapq

n = int(read())

def prime_list(n):
    sieve = [True] * n
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

ret = [0] * (n+1)
sieve = prime_list(n+1)
for i in sieve:
    ret[i] += 1

heapq.heapify(sieve)


while sieve:
    ptr1 = heapq.heappop(sieve)
    ret[ptr1] += 1
    qlen = len(sieve)
    for i in range(qlen):
        ptr2 = heapq.heappop(sieve)
        ret[ptr2] += 1
        if ptr1 + ptr2 <= n:
            if ret[ptr1] >= 3 and ret[ptr2] >= 3:
                heapq.heappush(sieve, ptr1+ptr2)
    print(ret)

print(sieve)