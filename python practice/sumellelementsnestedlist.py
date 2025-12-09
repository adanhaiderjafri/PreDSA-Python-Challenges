matrix = [[1,2,3], [4,5,6], [7,8,9]]
# Expected: 45
sum = 0
nested = [j for n in matrix for j in n]


for n in nested:
    sum = sum + n
print(f"sum of nested loop is : {sum}")