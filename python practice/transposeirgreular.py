from itertools import zip_longest
matrix = [
 [1, 2, 3, 4],
 [5, 6, 7],
 [9, 10, 11, 12, 11, 11]
]
transpose = [list(col) for col in zip_longest(*matrix,fillvalue=1)] 
print(transpose)
