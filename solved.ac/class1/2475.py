import sys

unique_num = list(map(int, sys.stdin.readline().strip().split()))

sum = 0
for num in unique_num:
    sum += pow(num, 2)
print(sum % 10)
