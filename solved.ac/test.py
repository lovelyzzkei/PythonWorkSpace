a = [['a', 'b', 'c'], ['a', 'a', 'a']]
print(" ".join(x for x in a[1]))
print("\n".join([" ".join(a[i]) for i in range(len(a))]))