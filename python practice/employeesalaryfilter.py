# n = int(input("number: "))
# a=0
# b=1


# for i in range(n):
#     next = a+b
#     a=b
#     b=next
    
#     print(a,end=" ")
def fabonacci(n):
    a=0
    b=1
    for i in range(n):
        next = a+b
        a=b
        b=next
        print(a,end=" ")
fabonacci(8)