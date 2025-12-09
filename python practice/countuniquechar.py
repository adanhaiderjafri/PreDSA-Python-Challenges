words = ["apple","orange","mango","banana"]
dic = {}
seen = set()
counter = 0
for w in words:
    for k in w:
        if k not in seen:
            counter +=1
            seen.add(k)
    dic[w] = counter
print(dic)
        