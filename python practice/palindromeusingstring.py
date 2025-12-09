word = input("tell me word,So that i check weather its palindrome or not :").lower()
words="".join(word).replace(" ", "").replace(",","")
if words ==words[::-1]:
    print("word is palindrome")
else:
    print("not palindrome")