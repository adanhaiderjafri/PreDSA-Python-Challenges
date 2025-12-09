a = {"x": 2, "y": 3}
b = {"y": 4, "z": 1}
dic = {}
for k,v in a.items():
    dic[k]=v
print(dic)
for k,v in b.items():
    dic[k] = dic.get(k,0)+v
print(dic)