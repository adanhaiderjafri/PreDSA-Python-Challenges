n = int(input("give me first number"))
m = int(input("give me second number"))
for i in range(n,0,-1):
    if m%i==0 and n%i==0:
       break
print(i)
