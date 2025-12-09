word = input("tell me word to check is it palindrome or not: ")
is_palindrome = True
if word==word[::-1]:
    print("yes")
else:
   print("nope")