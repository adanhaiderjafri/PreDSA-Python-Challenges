matrix = [
 [1, 2, 3, 4],
 [5, 6, 7,9],
 [9, 10, 11, 12]
]
transpose = [[rows[i] for rows in matrix] for i in range(4)]
print(transpose)