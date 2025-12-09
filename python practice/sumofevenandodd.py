# n = int(input("number :"))
# even =0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even = even + i

#     if i%2!=0:
#         odd = odd + i
# print("sum of even numbers are:",even)
# print("sum of odd numbers are:",odd)
def sum_of_even_odd(n):
    even = 0
    odd = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            even += i
        else:
            odd += i

    print("sum of even numbers are:", even)
    print("sum of odd numbers are:", odd)

n = int(input("number: "))
sum_of_even_odd(n)


    