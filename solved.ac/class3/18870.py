import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().strip().split()))
X_ = sorted(list(set(X)))
zip_ = {X_[i]:i for i in range(len(X_))}

for item in X:
    print(zip_[item], end=" ")