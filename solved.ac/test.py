a = [1, 2, 3]
b = [2, 3, 4]
D = [i for i, j in zip(a, b) if i == j]
print(set(a).intersection(b))
