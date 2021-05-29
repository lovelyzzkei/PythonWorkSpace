import sys

# 함수화
def isPalindrome(length):
    for n in range(length // 2):
        if num[n] != num[length - 1 - n]:
            return False
    return True

num =  sys.stdin.readline().strip()

while num != "0":
    if isPalindrome(len(num)):
        print('yes')
    else:
        print('no')

    num =  sys.stdin.readline().strip()
