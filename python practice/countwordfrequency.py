text = "Apple banana apple Banana orange apple".lower().split()
dic = {}
for t in text:
    dic[t] =dic.get(t,0)+1
print(dic)