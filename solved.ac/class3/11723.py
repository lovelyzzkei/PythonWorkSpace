import sys

S = 0

def check(x):
    k = int(bin(S & (1 << x)), 2)
    if pow(2, x) == k:
        print(1)
    else:
        print(0)

def empty():
    global S
    S = 0

def all():
    global S
    S = pow(2, 21) - 2

def add(x):
    global S
    S = int(bin(S | (1 << x)), 2)

def remove(x):
    global S
    S = int(bin(S & ~(1 << x)), 2)

def toggle(x):
    global S
    S = int(bin(S ^ (1 << x)), 2)


M = int(sys.stdin.readline())


for _ in range(M):
    operation = sys.stdin.readline().split()
    
    if operation[0] == 'check':
        check(int(operation[1]))
    elif operation[0] == 'empty':
        empty()
    elif operation[0] == 'all':
        all()
    elif operation[0] == 'add':
        add(int(operation[1]))
    elif operation[0] == 'remove':
        remove(int(operation[1]))
    elif operation[0] == 'toggle':
        toggle(int(operation[1]))