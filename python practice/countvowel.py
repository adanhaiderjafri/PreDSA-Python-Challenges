word  = input("tell me a word :").lower()
count = 0
words = "".join(word.replace(" ","").replace(",",""))
for w in words:

    if w in  "aeiou"  :
        count = count +1
print(count)




    