n = int(input("number:" ))
is_prime = True
if n < 1:
    is_prime = False
if n >1:
    for i in range(2,n):
        if n%i==0:
            is_prime = False
            break
if is_prime:
    print(n,"prime")
else:
    print(n,"not prime")

