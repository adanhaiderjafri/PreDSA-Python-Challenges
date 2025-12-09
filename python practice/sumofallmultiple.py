j= 0
n = int(input("number:"))
for i in range(1,n):
    if i%3==0 or i%5==0:
        j = j+i
print(j)