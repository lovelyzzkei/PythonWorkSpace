import sys; read = sys.stdin.readline

t = read().strip()
target = read().strip()
temp = []
for i in range(len(target)):
    temp.append(target[i])
target = temp
s = []; i = 0

while i < len(t):
    s.append(t[i])
    i += 1
    if len(s) < len(target): 
        continue
    if s[-len(target):] == target:
        for j in range(len(target)):
            s.pop()

if len(s) == 0:
    print("FRULA")
else:
    print("".join(x for x in s))


