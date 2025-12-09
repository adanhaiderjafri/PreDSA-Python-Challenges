numbers = [1,2,3,4,5,6]
# Expected: [4,16,36]
square = [n**2 for n in numbers if n%2==0]
print(f"square of even number is : {square}")