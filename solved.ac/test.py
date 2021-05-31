import sys

a = [[0, 0, 1], 
     [0, 0, 2],
     [1, 0, 2]]

print([col[1:3] for col in a[0:2]])