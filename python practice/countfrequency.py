sentence  = "I love Python and I love coding".split()

fre = {}
for ch in sentence:
    fre[ch] = fre.get(ch,0)+1
print(fre)
