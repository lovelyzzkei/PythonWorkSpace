import sys; read = sys.stdin.readline

n = int(read())

def prime_list(n):
    sieve = [True] * n
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

prime_number = prime_list(n+1)
plen = len(prime_number)
pSum = [0] * (plen+1)
for i in range(1, plen+1):
    pSum[i] = pSum[i-1] + prime_number[i-1]

ptr1 = 0; ptr2 = 1; ans = 0
while ptr1 < ptr2 and ptr2 <= plen:
    partial_sum = pSum[ptr2] - pSum[ptr1]
    if partial_sum <= n:
        if partial_sum == n:
            ans += 1
        ptr2 += 1
    else:
        ptr1 += 1

print(ans)