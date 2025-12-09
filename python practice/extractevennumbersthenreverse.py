# numbers = [10, 15, 20, 25, 30]
# lis = []
# for n in numbers:
#     if n%2==0:
#         lis.append(n)

# left = 0
# right = len(lis) -1
# while left < right:
#     lis[left] , lis[right] = lis[right] , lis[left]
#     left = left+1
#     right = right -1
# print(lis)
def reverse(numbers):
    lis = []
    for n in numbers:
        if n%2==0:
            lis.append(n)
    left = 0
    right = len(lis)-1
    while left > right :
        lis[left] , lis[right] = lis[right], lis[left]
        left = left-1
        right = right +1
    return lis
numbers  = [10,15,20,30,40,50]
result = reverse(numbers)
print(result)
