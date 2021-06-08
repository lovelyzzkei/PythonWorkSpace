import sys; read = sys.stdin.readline

def factorial(n):
    num_two = 0
    num_five = 0

    for i in range(1, n+1):
        num1 = i; num2 = i
        # 2의 개수 구하기
        while num1 / 2 == num1 // 2:
            num1 //= 2
            num_two += 1
        
        while num2 / 5 == num2 // 5:
            num2 //= 5
            num_five += 1
        
    print(min(num_two, num_five))


factorial(int(read()))